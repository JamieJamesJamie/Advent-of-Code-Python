"""Tests for Day2 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2015.day_02.day_02 import Day2
from tests.year_2015.abstract_test_day_2015 import AbstractTestDay2015


class TestDay(AbstractTestDay2015):
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

        :return: The Solver class that is being tested.
        """
        return Day2

    @pytest.mark.parametrize(
        "example, parsed",
        ((1, ((2, 3, 4),)), (2, ((1, 1, 10),)), (3, ((2, 3, 4), (1, 1, 10)))),
        indirect=["example"],
    )
    def test_parse_example(self, example, parsed):
        """Test that example input is parsed correctly.

        :param example: The actual parsed input from example file.
        :param parsed: The expected parsed input from example file.
        """
        assert example == parsed

    @pytest.mark.parametrize(
        "example, result", ((1, 58), (2, 43), (3, 101)), indirect=["example"]
    )
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize(
        "example, result", ((1, 34), (2, 14), (3, 48)), indirect=["example"]
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
