"""Solutions for day 5."""

from collections.abc import Iterable
from functools import cmp_to_key

from advent_of_code.helper.solver import Solver


class ParsedInput:
    """Represents the parsed input."""

    # pylint: disable=too-few-public-methods

    def __init__(self, puzzle_input: str):
        page_ordering_rules_lines, update_page_numbers_lines = (
            tuple(puzzle_input_sections.splitlines())
            for puzzle_input_sections in puzzle_input.split("\n\n")
        )

        self._page_ordering_rules = set()
        for rule in page_ordering_rules_lines:
            page_numbers = rule.split("|")
            self._page_ordering_rules.add((int(page_numbers[0]), int(page_numbers[1])))

        self._update_page_numbers = tuple(
            tuple(int(page_number) for page_number in update.split(","))
            for update in update_page_numbers_lines
        )

    def _sort_update(self, update: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(
            sorted(
                update,
                key=cmp_to_key(
                    lambda a, b: (-1 if (a, b) in self._page_ordering_rules else 1)
                ),
            )
        )

    def _iterate_middle_pages(self, is_ordered: bool) -> Iterable[int]:
        for update in self._update_page_numbers:
            sorted_update = self._sort_update(update)

            if (update == sorted_update) == is_ordered:
                yield sorted_update[int(len(update) / 2)]

    def sum_middle_pages(self, is_ordered: bool) -> int:
        """Sums the middle pages.

        :param is_ordered: Whether to sum the correctly-ordered updates
            or the incorrectly-ordered updates.
        :return: The sum of the middle pages.
        """
        return sum(self._iterate_middle_pages(is_ordered))


class Day5(Solver):
    """Solver for day 5."""

    @staticmethod
    def parse(puzzle_input: str) -> ParsedInput:
        """Parse input for puzzle 5.

        :param puzzle_input: Input to parse.
        :return: The parsed input.
        """
        return ParsedInput(puzzle_input)

    @staticmethod
    def part1(parsed_input: ParsedInput) -> int:
        """Solves part 1.

        :param parsed_input: The parsed input.
        :return: The sum of the middle page numbers from the correctly-
            ordered updates.
        """
        return parsed_input.sum_middle_pages(is_ordered=True)

    @staticmethod
    def part2(parsed_input: ParsedInput) -> int:
        """Solves part 2.

        :param parsed_input: The parsed input.
        :return: The sum of the middle page numbers from the
            incorrectly-ordered updates.
        """
        return parsed_input.sum_middle_pages(is_ordered=False)
