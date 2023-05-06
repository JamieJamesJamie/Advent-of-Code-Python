"""Tests for Day11 Solution class."""


import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_11.day_11 import Day11, Monkey


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay11(AbstractTestDay):
    """Test class for testing day 11."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 11

    @staticmethod
    def solver() -> type[Day11]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day11

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == (
            Monkey(0, [79, 98], "  Operation: new = old * 19", 23, 2, 3),
            Monkey(1, [54, 65, 75, 74], "  Operation: new = old + 6", 19, 2, 0),
            Monkey(2, [79, 60, 97], "  Operation: new = old * old", 13, 1, 3),
            Monkey(3, [74], "  Operation: new = old + 3", 17, 0, 1),
        )

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 10_605

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 2_713_310_158
