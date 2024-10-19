"""Solutions for day 1."""

from collections.abc import Iterable

from advent_of_code.helper.solver import Solver


class Day1(Solver):
    """Solver for day 1."""

    @staticmethod
    def parse(puzzle_input: str) -> Iterable[int]:
        """Parse input for puzzle 1.

        :param puzzle_input: Input to parse.
        :return: The floor increment for each direction in the
            instructions.
        """
        floor_increment_mappings = {"(": 1, ")": -1}

        return (floor_increment_mappings[direction] for direction in puzzle_input)

    @staticmethod
    def part1(parsed_input: Iterable[int]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The floor that Santa should deliver the presents to.
        """
        return sum(parsed_input)

    @staticmethod
    def part2(parsed_input: Iterable[int]) -> int | None:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The position in the instructions that causes Santa to
            first enter the basement, or None if Santa never makes it to
            the basement.
        """
        basement_floor = -1
        current_floor = 0

        for position, floor_increment in enumerate(parsed_input, 1):
            current_floor += floor_increment

            if current_floor == basement_floor:
                return position

        return None
