"""Solutions for day 5."""

import re
from collections.abc import Iterable

from advent_of_code.helper.solver import Solver


class Day5(Solver):
    """Solver for day 5."""

    FORBIDDEN_STRINGS = {"ab", "cd", "pq", "xy"}

    AT_LEAST_3_VOWELS_REGEX = ".*".join(["[aeiou]"] * 3)
    CONTAINS_AT_LEAST_1_REPEATING_LETTER_REGEX = r"(?P<character>\w)(?P=character)"
    DOES_NOT_CONTAIN_FORBIDDEN_STRING_REGEX = f"^((?!{'|'.join(FORBIDDEN_STRINGS)}).)*$"

    CONTAINS_NON_OVERLAPPING_PAIR_OF_LETTERS_REGEX = r"(?P<pair>\w\w).*(?P=pair)"
    CONTAINS_REPEATED_LETTER_WITH_1_LETTER_INBETWEEN_REGEX = (
        r"(?P<outer>\w)\w(?P=outer)"
    )

    @staticmethod
    def _num_nice_strings(parsed_input: str, regexes: Iterable[str]) -> int:
        all_regexes = "".join(rf"(?=^.*{regex}.*$)" for regex in regexes)
        matches = re.findall(all_regexes, parsed_input, re.MULTILINE)
        return len(matches)

    @staticmethod
    def parse(puzzle_input: str) -> str:
        """Parse input for puzzle 5.

        :param puzzle_input: Input to parse.
        :return: The strings to process.
        """
        return puzzle_input

    @staticmethod
    def part1(parsed_input: str) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The total number of nice strings.
        """
        return Day5._num_nice_strings(
            parsed_input,
            (
                Day5.AT_LEAST_3_VOWELS_REGEX,
                Day5.CONTAINS_AT_LEAST_1_REPEATING_LETTER_REGEX,
                Day5.DOES_NOT_CONTAIN_FORBIDDEN_STRING_REGEX,
            ),
        )

    @staticmethod
    def part2(parsed_input: str) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The total number of nice strings.
        """
        return Day5._num_nice_strings(
            parsed_input,
            (
                Day5.CONTAINS_NON_OVERLAPPING_PAIR_OF_LETTERS_REGEX,
                Day5.CONTAINS_REPEATED_LETTER_WITH_1_LETTER_INBETWEEN_REGEX,
            ),
        )
