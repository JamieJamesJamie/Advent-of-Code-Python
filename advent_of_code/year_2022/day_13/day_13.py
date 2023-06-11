"""Solutions for day 13."""


import ast
import functools
from collections.abc import Iterable, Sequence
from typing import Any

import numpy as np
from anytree import Node, RenderTree

from advent_of_code.helper.solver import Solver


class Day13(Solver):
    """Solver for day 13."""

    @staticmethod
    def _render_tree(node: Node) -> str:
        """Renders the :param:`node` and its children to a pretty string.

        :param node: The node to render from.
        :return: A pretty string that can be printed to see a visual representation of
            the tree starting at the provided node.
        """
        return "\n".join(f"{pre}{node_i.name}" for pre, _, node_i in RenderTree(node))

    @staticmethod
    def _print_tree(node: Node) -> None:
        """Prints the tree from the root :param:`node`.

        :param node: The node to render and print from.
        """
        print(Day13._render_tree(node))

    @staticmethod
    def _compare_integers(left: int, right: int, parent_node: Node) -> bool | None:
        """Returns whether the inputs :param:`left` and :param:`right` are in
        the correct order.

        :param left: The left input.
        :param right: The right input.
        :param parent_node: The node for debugging purposes.
        :return: Whether the left input is lower than the right input, or None if the
            inputs are the same.
        """
        current_node = Node(f"Compare {left} vs {right}", parent=parent_node)

        if left == right:
            return None

        right_order = left < right

        Node(
            f"{'Left' if right_order else 'Right'} side is smaller, so inputs are"
            f"{'' if right_order else ' not'} in the right order",
            parent=current_node,
        )

        return right_order

    @staticmethod
    def _compare_lists(
        left_list: Sequence[Any],
        right_list: Sequence[Any],
        parent_node: Node | None = None,
    ) -> tuple[bool | None, Node]:
        """Returns whether the inputs :param:`left_list` and
        :param:`right_list` are in the correct order.

        :param left_list: The left input.
        :param right_list: The right input.
        :param parent_node: The node for debugging purposes.
        :return: Whether the inputs are in the correct order, or None if the inputs are
            the same.
        """
        current_node = Node(f"Compare {left_list} vs {right_list}", parent=parent_node)

        for left_elem, right_elem in zip(left_list, right_list):
            if isinstance(left_elem, int) and isinstance(right_elem, int):
                right_order = Day13._compare_integers(
                    left_elem, right_elem, current_node
                )

                if right_order is not None:
                    return right_order, current_node

            elif isinstance(left_elem, Sequence) and isinstance(right_elem, Sequence):
                right_order, _ = Day13._compare_lists(
                    left_elem, right_elem, current_node
                )

                if right_order is not None:
                    return right_order, current_node

            elif isinstance(left_elem, int) and isinstance(right_elem, Sequence):
                intermediate_node = Node(
                    f"Compare {left_elem} vs {right_elem}", parent=current_node
                )
                Node(
                    f"Mixed types; convert left ({left_elem}) to [{left_elem}] "
                    "and retry comparison",
                    parent=intermediate_node,
                )
                right_order, _ = Day13._compare_lists(
                    [left_elem], right_elem, intermediate_node
                )

                if right_order is not None:
                    return right_order, current_node

            elif isinstance(left_elem, Sequence) and isinstance(right_elem, int):
                intermediate_node = Node(
                    f"Compare {left_elem} vs {right_elem}", parent=current_node
                )
                Node(
                    f"Mixed types; convert right ({right_elem}) to [{right_elem}] "
                    "and retry comparison",
                    parent=intermediate_node,
                )
                right_order, _ = Day13._compare_lists(
                    left_elem, [right_elem], intermediate_node
                )

                if right_order is not None:
                    return right_order, current_node

        if len(left_list) != len(right_list):
            right_order = len(left_list) < len(right_list)

            Node(
                f"{'Left' if right_order else 'Right'} side ran out of items, "
                f"so inputs are {'' if right_order else 'not '}in the right order",
                parent=current_node,
            )

            return right_order, current_node

        return None, current_node

    @staticmethod
    def _sort(item1: list[Any], item2: list[Any]):
        """
        Returns whether :param:`item1` is smaller, larger or the same size as
        :param:`item2`.

        :param item1: Item to compare.
        :param item2: Items to compare.
        :return: -1 if item1 is smaller than item2. 1 if item1 is larger than item2.
            0 if item1 is the same size as item2.
        """
        result, _ = Day13._compare_lists(item1, item2)
        return 0 if result is None else -1 if result else 1

    @staticmethod
    def parse(puzzle_input: str) -> tuple[tuple[list[Any], ...], ...]:
        """Parse input for puzzle 13.

        :param puzzle_input: Input to parse.
        :return: Pairs of packets.
        """
        return tuple(
            tuple(ast.literal_eval(packets) for packets in pair.split("\n"))
            for pair in puzzle_input.split("\n\n")
        )

    @staticmethod
    def part1(parsed_input: Iterable[Iterable[list[Any]]]) -> int:
        """Solves part 1.

        :param parsed_input: Pairs of packets.
        :return: The sum of the indices of the pairs where the left
            packet is smaller than the right packet.
        """
        # for list_index, (left_list, right_list) in enumerate(parsed_input, start=1):
        #     right_order, root = Day13._compare_lists(left_list, right_list)
        #
        #     print(f"== Pair {list_index} ==")
        #     Day13.print_tree(root)
        #     print()
        #     print(f"Right order: {right_order}")
        #     print()
        #     print()

        return sum(
            list_index
            for list_index, (left_list, right_list) in enumerate(parsed_input, start=1)
            if Day13._compare_lists(left_list, right_list)[0]
        )

    @staticmethod
    def part2(parsed_input: Iterable[Sequence[list[Any]]]) -> int:
        """Solves part 2.

        :param parsed_input: Pairs of packets.
        :return: The decoder key for the distress signal.
        """
        additional_input = [[[[2]], [[6]]]]
        new_parsed_input = [
            pair for pairs in list(parsed_input) + additional_input for pair in pairs
        ]

        new_parsed_input.sort(key=functools.cmp_to_key(Day13._sort))

        return int(
            np.prod(
                [new_parsed_input.index(packet) + 1 for packet in additional_input[0]]
            )
        )
