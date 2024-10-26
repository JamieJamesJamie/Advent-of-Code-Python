"""Tests for Day4 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2015.day_04.day_04 import Day4
from tests.year_2015.abstract_test_day_2015 import AbstractTestDay2015


class TestDay(AbstractTestDay2015):
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

    @pytest.mark.parametrize(
        "example, parsed", ((1, "abcdef"), (2, "pqrstuv")), indirect=["example"]
    )
    def test_parse_example(self, example, parsed):
        """Test that example input is parsed correctly.

        :param example: The actual parsed input from example file.
        :param parsed: The expected parsed input from example file.
        """
        assert example == parsed

    @pytest.mark.parametrize(
        "example, result", ((1, 609043), (2, 1048970)), indirect=["example"]
    )
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize(
        "example, result", ((1, 6742839), (2, 5714438)), indirect=["example"]
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
