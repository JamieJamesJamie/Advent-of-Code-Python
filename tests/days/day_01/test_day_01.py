"""Tests for Day1 Solution class."""


import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_01.day_01 import Day1


@pytest.mark.usefixtures("example1")
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

    def test_parse_example1(self, example1):
        """Test that example1 input is parsed correctly.

        :param example1: Parsed input from example1 file.
        """
        assert example1 == (6_000, 4_000, 11_000, 24_000, 10_000)

    def test_part1_example1(self, example1):
        """Test part 1 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part1(example1) == 24_000

    def test_part2_example1(self, example1):
        """Test part 2 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part2(example1) == 45_000
