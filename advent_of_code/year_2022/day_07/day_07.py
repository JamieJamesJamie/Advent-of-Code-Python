"""Solutions for day 7."""

from collections.abc import Sequence
from functools import partial
from typing import Any

from anytree import Node as AnyTreeNode
from anytree import PostOrderIter, RenderTree

from advent_of_code.helper.solver import Solver


class Node(AnyTreeNode):
    """Tree node to represent a file or directory within a file system."""

    # pylint: disable=too-few-public-methods

    file_size: int

    def __init__(
        self,
        name: Any,
        file_size: int = 0,
        parent: Any | None = None,
        children: Any | None = None,
        **kwargs: Any,
    ):
        super().__init__(name, parent, children, file_size=file_size, **kwargs)


class Day7(Solver):
    """Solver for day 7."""

    @staticmethod
    def process_file(line: Sequence[str], current_node: Node) -> None:
        """Adds file or directory specified by :param:`line` as a child to the
        given :param:`current_node`.

        If the specified file or directory is already a child of :param:`current_node`,
        then the file or directory is not added as a child to :param:`current_node`.

        :param line: Line from the puzzle input describing the file or directory.
        :param current_node: The node to add the child to.
        """
        if all(line[1] != child.name for child in current_node.children):
            Node(
                name=line[1],
                parent=current_node,
                file_size=0 if line[0] == "dir" else int(line[0]),
            )

    @staticmethod
    def change_directory(line: Sequence[str], current_node: Node) -> Node:
        """Changes directory from the :param:`current_node` using the
        instruction provided in :param:`line`.

        :param line: The change directory (cd) instruction as seen in
            the puzzle input.
        :param current_node: The node to traverse from.
        :return: The node that was traversed to.
        """
        directory = line[2]

        if directory == "/":
            return current_node.root

        if directory == "..":
            return current_node.parent

        for child in current_node.children:
            if directory == child.name:
                return child

        return Node(directory, parent=current_node)

    @staticmethod
    def render_tree(node: Node) -> str:
        """Renders the :param:`node` and its children to a pretty string.

        :param node: The node to render from.
        :return: A pretty string that can be printed to see a visual
            representation of the tree starting at the provided node.
        """
        return "\n".join(
            f"{pre}{node_i.name}"
            f" ("
            f"{'file' if node_i.is_leaf else 'dir'}, "
            f"file_size={node_i.file_size}"
            f")"
            for pre, _, node_i in RenderTree(node)
        )

    @staticmethod
    def print_tree(node: Node) -> None:
        """Prints the tree from the root :param:`node`.

        :param node: The node to render and print from.
        """
        print(Day7.render_tree(node))

    @staticmethod
    def post_order_function_with_file_size_limit(
        node: Node, file_size_limit: int | None = None
    ) -> bool:
        """Calculates the file size of the :param:`node` and returns whether
        the :param:`node` should be used for traversal.

        The :param:`node` will be used for traversal if the :param:`node`'s file size
        is less than or equal to the :param:`file_size_limit`.
        Otherwise, if :param:`file_size_limit` is :code:`None`,
        this function will always return :code:`True`.

        :param node: The node to check.
        :param file_size_limit: The file size limit to filter on.
        :return: Whether the node should be included in the filter.
        """
        if not node.is_leaf:
            node.file_size = sum(child.file_size for child in node.children)

        return file_size_limit is None or (
            node.file_size <= file_size_limit and not node.is_leaf
        )

    @staticmethod
    def parse(puzzle_input: str) -> Node:
        """Parse input for puzzle 7.

        :param puzzle_input: Input to parse.
        :return: The root directory of the tree described in the puzzle
            input.
        """
        root = Node("/")
        current_node = root

        for line_string in puzzle_input.splitlines():
            line = line_string.split(" ")

            if line[0] != "$":
                Day7.process_file(line, current_node)
            elif line[1] == "cd":
                current_node = Day7.change_directory(line, current_node)

        # Calculate each node's file_size
        _ = sum(
            node.file_size
            for node in PostOrderIter(
                root, filter_=Day7.post_order_function_with_file_size_limit
            )
        )

        return root

    @staticmethod
    def part1(parsed_input: Node) -> int:
        """Solves part 1.

        :param parsed_input: The root directory of the tree described in
            the puzzle input.
        :return: The sum of the directories' total file sizes that are
            less than or equal to 100,000.
        """
        return sum(
            node.file_size
            for node in PostOrderIter(
                parsed_input,
                filter_=partial(
                    Day7.post_order_function_with_file_size_limit,
                    file_size_limit=100_000,
                ),
            )
        )

    @staticmethod
    def part2(parsed_input: Node) -> int:
        """Solves part 2.

        :param parsed_input: The root directory of the tree described in
            the puzzle input.
        :return: The total file size of the smallest directory that, if
            deleted, would free up enough space on the filesystem to run
            the update.
        """

        total_disk_space = 70_000_000
        required_unused_space = 30_000_000
        min_directory_deletion_file_size = required_unused_space - (
            total_disk_space - parsed_input.file_size
        )

        answer_node = min(
            (
                node
                for node in PostOrderIter(
                    parsed_input,
                    filter_=lambda n: not n.is_leaf
                    and n.file_size >= min_directory_deletion_file_size,
                )
            ),
            key=lambda n: n.file_size,
        )

        return answer_node.file_size
