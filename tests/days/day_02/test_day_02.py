"""Tests for Day2 Solution class."""


import pytest

from advent_of_code_2022.days.day_02.day_02 import Day2
from tests.days.helper.abstract_test_day import AbstractTestDay


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay2(AbstractTestDay):
    """Test class for testing day 2."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 2

    @staticmethod
    def solver() -> type[Day2]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day2

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == (("A", "Y"), ("B", "X"), ("C", "Z"))

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 15

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 12
