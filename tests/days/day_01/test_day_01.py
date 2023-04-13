"""Tests for Day1 Solution class."""


import pytest

from advent_of_code_2022.days.day_01.day_01 import Day1
from tests.days.helper.abstract_test_day import AbstractTestDay


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay1(AbstractTestDay):
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

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == (6_000, 4_000, 11_000, 24_000, 10_000)

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 24_000

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 45_000
