"""Tests for Day5 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2015.day_05.day_05 import Day5
from tests.year_2015.abstract_test_day_2015 import AbstractTestDay2015


class TestDay(AbstractTestDay2015):
    """Test class for testing day 5."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 5

    @staticmethod
    def solver() -> type[Day5]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day5

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, ("ugknbfddgicrmopn",)),
            (2, ("aaa",)),
            (3, ("jchzalrnumimnmhp",)),
            (4, ("haegwjzuvuyypxyu",)),
            (5, ("dvszwmarrgswjxmb",)),
            (
                6,
                (
                    "ugknbfddgicrmopn",
                    "aaa",
                    "jchzalrnumimnmhp",
                    "haegwjzuvuyypxyu",
                    "dvszwmarrgswjxmb",
                ),
            ),
            (7, ("qjhvhtzxzqqjkmpb",)),
            (8, ("xxyxx",)),
            (9, ("uurcxstgmygtbstg",)),
            (10, ("ieodomkazucvgmuy",)),
            (11, ("qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy")),
        ),
        indirect=["example"],
    )
    def test_parse_example(self, example, parsed):
        """Test that example input is parsed correctly.

        :param example: The actual parsed input from example file.
        :param parsed: The expected parsed input from example file.
        """
        assert example == parsed

    @pytest.mark.parametrize(
        "example, result",
        ((1, 1), (2, 1), (3, 0), (4, 0), (5, 0), (6, 2)),
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
        ((7, 1), (8, 1), (9, 0), (10, 0), (11, 2)),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
