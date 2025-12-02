"""Tests for Day1 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2025.day_01.day_01 import Day1
from tests.year_2025.abstract_test_day_2025 import AbstractTestDay2025


class TestDay(AbstractTestDay2025):
    """Test class for testing day 1."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 1

    @staticmethod
    def solver() -> type[Day1]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day1

    @pytest.mark.parametrize(
        "example, result",
        ((1, (-68, -30, 48, -5, 60, -55, -1, -99, 14, -82)),),
        indirect=["example"],
    )
    def test_parse_example(self, example, result):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert tuple(example) == result

    @pytest.mark.parametrize("example, result", ((1, 3),), indirect=["example"])
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize(
        "example, result",
        ((1, 6), (2, 10)),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
