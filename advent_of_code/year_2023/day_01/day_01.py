"""Solutions for day 2."""


from typing import Iterable

from advent_of_code.helper.solver import Solver


class Day1(Solver):
    """Solver for day 1."""

    _NUMBER_MAPPINGS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    @staticmethod
    def _part1_1_line(parsed_input: Iterable[str]) -> int:
        """Part 1 in 1 line 😎.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """
        return sum(
            (10 * int(next(x for x in string if x.isdigit())))
            + int(next(x for x in reversed(string) if x.isdigit()))
            for string in parsed_input
        )

    @staticmethod
    def _find_number_start(sequence: str) -> int:
        for index, character in enumerate(sequence):
            if character.isdigit():
                return int(character)

            for key, value in Day1._NUMBER_MAPPINGS.items():
                if str(sequence[index:]).startswith(key):
                    return value

        return 0

    @staticmethod
    def _find_number_end(sequence: str) -> int:
        for index, character in enumerate(sequence[::-1]):
            if character.isdigit():
                return int(character)

            for key, value in Day1._NUMBER_MAPPINGS.items():
                if str(sequence[: len(sequence) if index == 0 else -index]).endswith(
                    key
                ):
                    return value

        return 0

    @staticmethod
    def parse(puzzle_input: str) -> tuple[str, ...]:
        """Parse input for puzzle 1.

        :param puzzle_input: Input to parse.
        :return: The lines to use for calibration.
        """
        return tuple(puzzle_input.split("\n"))

    @staticmethod
    def part1(parsed_input: Iterable[str]) -> int:
        """Solves part 1.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """
        result = 0

        for string in parsed_input:
            first_digit = next(x for x in string if x.isdigit())
            last_digit = next(x for x in reversed(string) if x.isdigit())
            result += (10 * int(first_digit)) + int(last_digit)

        return result

    @staticmethod
    def part2(parsed_input: Iterable[str]) -> int:
        """Solves part 2.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """
        result = 0

        for string in parsed_input:
            first_digit = Day1._find_number_start(string)
            last_digit = Day1._find_number_end(string)
            result += (10 * first_digit) + last_digit

        return result
