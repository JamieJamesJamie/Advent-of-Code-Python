"""Tests for Day12 Solution class."""


import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_12.day_12 import Day12


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay12(AbstractTestDay):
    """Test class for testing day 12."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 8

    @staticmethod
    def solver() -> type[Day12]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day12

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == 1

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 31

    def test_part2_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 29
