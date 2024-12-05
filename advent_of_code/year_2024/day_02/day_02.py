"""Solutions for day 2."""

from collections.abc import Iterable
from itertools import combinations, pairwise

from advent_of_code.helper.solver import Solver


class Day2(Solver):
    """Solver for day 2."""

    @staticmethod
    def _check_levels_sorted(levels: tuple[int, ...], reverse) -> bool:
        return levels == tuple(sorted(levels, reverse=reverse))

    @staticmethod
    def _is_safe_report(report: tuple[int, ...]) -> bool:
        return (
            Day2._check_levels_sorted(report, False)
            or Day2._check_levels_sorted(report, True)
        ) and all(
            1 <= abs(left_level - right_level) <= 3
            for left_level, right_level in pairwise(report)
        )

    @staticmethod
    def parse(puzzle_input: str) -> Iterable[tuple[int, ...]]:
        """Parse input for puzzle 2.

        :param puzzle_input: Input to parse.
        :return: The reports.
        """
        return (
            tuple(int(level) for level in report.split())
            for report in puzzle_input.splitlines()
        )

    @staticmethod
    def part1(parsed_input: Iterable[tuple[int, ...]]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The number of safe reports.
        """
        return sum(Day2._is_safe_report(report) for report in parsed_input)

    @staticmethod
    def part2(parsed_input: Iterable[tuple[int, ...]]) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The number of safe reports.
        """
        return sum(
            any(
                (
                    Day2._is_safe_report(report),
                    *(
                        Day2._is_safe_report(report_subset)
                        for report_subset in combinations(report, len(report) - 1)
                    ),
                )
            )
            for report in parsed_input
        )
