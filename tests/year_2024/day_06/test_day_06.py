"""Tests for Day6 Solution class."""

import pytest

from advent_of_code.year_2024.day_06.day_06 import Day6
from tests.year_2024.abstract_test_day_2024 import AbstractTestDay2024


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2024):
    """Test class for testing day 6."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 6

    @staticmethod
    def solver() -> type[Day6]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day6

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == 4

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 41

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 123
