"""Tests for Day1 Solution class."""


import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_03.day_03 import Day3


@pytest.mark.usefixtures("example1")
class TestDay3(AbstractTestDay):
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

    def test_parse_example1(self, example1):
        """Test that example1 input is parsed correctly.

        :param example1: Parsed input from example1 file.
        """
        assert example1 == (
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        )

    def test_part1_example1(self, example1):
        """Test part 1 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part1(example1) == 157

    def test_part2_example1(self, example1):
        """Test part 2 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part2(example1) == 70
