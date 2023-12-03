"""Tests for Day3 Solution class."""


import pytest

from advent_of_code.year_2023.day_03.day_03 import Day3
from tests.year_2023.abstract_test_day_2023 import AbstractTestDay2023


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2023):
    """Test class for testing day 3."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 3

    @staticmethod
    def solver() -> type[Day3]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day3

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == (6_000, 4_000, 11_000, 24_000, 10_000)

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 4_361

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 467_835
