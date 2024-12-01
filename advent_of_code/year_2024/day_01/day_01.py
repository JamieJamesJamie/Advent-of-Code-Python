"""Solutions for day 1."""

from collections.abc import Iterable, Iterator

from advent_of_code.helper.solver import Solver


class Day1(Solver):
    """Solver for day 1."""

    @staticmethod
    def parse(puzzle_input: str) -> Iterator[Iterable[int]]:
        """Parse input for puzzle 1.

        :param puzzle_input: Input to parse.
        :return: The lists of location IDs.
        """
        return zip(
            *(
                (int(number) for number in line.split())
                for line in puzzle_input.splitlines()
            )
        )

    @staticmethod
    def part1(parsed_input: Iterator[Iterable[int]]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The total distance between the lists.
        """
        return sum(
            abs(list1_element - list2_element)
            for list1_element, list2_element in zip(
                *(sorted(location_list) for location_list in parsed_input)
            )
        )

    @staticmethod
    def part2(parsed_input: Iterator[Iterable[int]]) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The similarity score of the lists.
        """
        lists = tuple(parsed_input)
        left_list = lists[0]
        right_list = tuple(lists[1])

        return sum(
            left_list_element * right_list.count(left_list_element)
            for left_list_element in left_list
        )
