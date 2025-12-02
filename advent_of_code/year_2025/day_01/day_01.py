"""Solutions for day 1."""

from collections.abc import Iterable

from advent_of_code.helper.solver import Solver


class Day1(Solver):
    """Solver for day 1."""

    @staticmethod
    def parse(puzzle_input: str) -> Iterable[int]:
        """Parse input for puzzle 1.

        :param puzzle_input: Input to parse.
        :return: The rotations to perform on the dial.
        """
        return (
            int(line)
            for line in puzzle_input.replace("R", "+").replace("L", "-").splitlines()
        )

    @staticmethod
    def part1(parsed_input: Iterable[int]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The number of times the dial points at 0 after
            following each rotation step.
        """
        password = 0
        dial_pointer = 50

        for rotation in parsed_input:
            dial_pointer = (dial_pointer + rotation) % 100

            if dial_pointer == 0:
                password += 1

        return password

    @staticmethod
    def part2(parsed_input: Iterable[int]) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The number of times the dial points at 0 during each
            rotation step.
        """
        password = 0
        dial_pointer = 50

        for rotation in parsed_input:
            for _ in range(abs(rotation)):
                dial_pointer += 1 if rotation >= 0 else -1

                if dial_pointer % 100 == 0:
                    password += 1

        return password
