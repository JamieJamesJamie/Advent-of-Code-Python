"""Tests for Day3 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2015.day_03.day_03 import Day3
from tests.year_2015.abstract_test_day_2015 import AbstractTestDay2015


class TestDay(AbstractTestDay2015):
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

    @pytest.mark.parametrize(
        "example, parsed",
        ((1, ">"), (2, "^>v<"), (3, "^v^v^v^v^v"), (4, "^v")),
        indirect=["example"],
    )
    def test_parse_example(self, example, parsed):
        assert example == parsed

    @pytest.mark.parametrize(
        "example, result", ((1, 2), (2, 4), (3, 2), (4, 2)), indirect=["example"]
    )
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize(
        "example, result", ((1, 2), (2, 3), (3, 11), (4, 3)), indirect=["example"]
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
