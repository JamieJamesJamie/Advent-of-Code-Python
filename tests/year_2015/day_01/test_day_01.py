"""Tests for Day1 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2015.day_01.day_01 import Day1
from tests.year_2015.abstract_test_day_2015 import AbstractTestDay2015


class TestDay(AbstractTestDay2015):
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

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, (1, 1, -1, -1)),
            (2, (1, -1, 1, -1)),
            (3, (1, 1, 1)),
            (4, (1, 1, -1, 1, 1, -1, 1)),
            (5, (-1, -1, 1, 1, 1, 1, 1)),
            (6, (1, -1, -1)),
            (7, (-1, -1, 1)),
            (8, (-1, -1, -1)),
            (9, (-1, 1, -1, -1, 1, -1, -1)),
            (10, (-1,)),
            (11, (1, -1, 1, -1, -1)),
        ),
        indirect=["example"],
    )
    def test_parse_example(self, example, parsed):
        """Test that example input is parsed correctly.

        :param example: The actual parsed input from example file.
        :param parsed: The expected parsed input from example file.
        """
        assert tuple(example) == parsed

    @pytest.mark.parametrize(
        "example, result",
        (
            (1, 0),
            (2, 0),
            (3, 3),
            (4, 3),
            (5, 3),
            (6, -1),
            (7, -1),
            (8, -3),
            (9, -3),
            (10, -1),
            (11, -1),
        ),
        indirect=["example"],
    )
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize(
        "example, result",
        (
            (1, None),
            (2, None),
            (3, None),
            (4, None),
            (5, 1),
            (6, 3),
            (7, 1),
            (8, 1),
            (9, 1),
            (10, 1),
            (11, 5),
        ),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
