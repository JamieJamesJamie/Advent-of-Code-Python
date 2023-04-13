"""Tests for Day1 Solution class."""


import pytest
from tests.days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_03.day_03 import Day3


@pytest.mark.parametrize("example", [1], indirect=True)
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

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == (
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        )

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 157

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 70
