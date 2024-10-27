"""Solutions for day 5."""

import re
from collections.abc import Iterable

from advent_of_code.helper.solver import Solver


class Day5(Solver):
    """Solver for day 5."""

    FORBIDDEN_STRINGS = {"ab", "cd", "pq", "xy"}

    @staticmethod
    def _contains_at_least_3_vowels(string: str) -> bool:
        return sum(map(string.lower().count, "aeiou")) >= 3

    @staticmethod
    def _contains_at_least_1_repeating_letter(string: str) -> bool:
        return re.search(r"(\w)\1", string) is not None

    @staticmethod
    def _does_not_contain_forbidden_strings(string: str) -> bool:
        return not any(
            forbidden_string in string for forbidden_string in Day5.FORBIDDEN_STRINGS
        )

    @staticmethod
    def _is_nice_string_part_1(string: str) -> bool:
        return (
            Day5._contains_at_least_3_vowels(string)
            and Day5._contains_at_least_1_repeating_letter(string)
            and Day5._does_not_contain_forbidden_strings(string)
        )

    @staticmethod
    def _contains_a_pair_of_any_2_letters_without_overlapping(string: str) -> bool:
        return re.search(r"(\w\w).*\1", string) is not None

    @staticmethod
    def _contains_at_least_1_letter_which_repeats_with_1_letter_between_them(
        string: str,
    ) -> bool:
        return re.search(r"(\w)\w\1", string) is not None

    @staticmethod
    def _is_nice_string_part_2(string: str) -> bool:
        return Day5._contains_a_pair_of_any_2_letters_without_overlapping(
            string
        ) and Day5._contains_at_least_1_letter_which_repeats_with_1_letter_between_them(
            string
        )

    @staticmethod
    def parse(puzzle_input: str) -> tuple[str, ...]:
        """Parse input for puzzle 5.

        :param puzzle_input: Input to parse.
        :return: The strings to process.
        """
        return tuple(puzzle_input.splitlines())

    @staticmethod
    def part1(parsed_input: Iterable[str]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The total number of nice strings.
        """
        return sum(Day5._is_nice_string_part_1(string) for string in parsed_input)

    @staticmethod
    def part2(parsed_input: Iterable[str]) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The total number of nice strings.
        """
        return sum(Day5._is_nice_string_part_2(string) for string in parsed_input)
