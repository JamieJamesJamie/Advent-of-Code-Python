"""Tests for Day4 Solution class."""


import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_04.day_04 import Day4


@pytest.mark.usefixtures("example1")
class TestDay4(AbstractTestDay):
    """Test class for testing day 4."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 4

    @staticmethod
    def solver() -> type[Day4]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day4

    def test_parse_example1(self, example1):
        """Test that example1 input is parsed correctly.

        :param example1: Parsed input from example1 file.
        """
        assert example1 == (
            ({2, 3, 4}, {6, 7, 8}),
            ({2, 3}, {4, 5}),
            ({5, 6, 7}, {7, 8, 9}),
            ({2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}),
            ({6}, {4, 5, 6}),
            ({2, 3, 4, 5, 6}, {4, 5, 6, 7, 8}),
        )

    def test_part1_example1(self, example1):
        """Test part 1 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part1(example1) == 2

    def test_part2_example1(self, example1):
        """Test part 2 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part2(example1) == 4
