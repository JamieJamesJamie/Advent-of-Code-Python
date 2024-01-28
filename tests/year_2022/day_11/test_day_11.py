"""Tests for Day11 Solution class."""

import pytest

from advent_of_code.year_2022.day_11.day_11 import Day11, Monkey
from tests.year_2022.abstract_test_day_2022 import AbstractTestDay2022


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2022):
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
            Monkey(
                0,
                [79, 98],
                Monkey.POSSIBLE_OPERATORS["*"],
                "19",
                23,
                {True: 2, False: 3},
            ),
            Monkey(
                1,
                [54, 65, 75, 74],
                Monkey.POSSIBLE_OPERATORS["+"],
                "6",
                19,
                {True: 2, False: 0},
            ),
            Monkey(
                2,
                [79, 60, 97],
                Monkey.POSSIBLE_OPERATORS["*"],
                "old",
                13,
                {True: 1, False: 3},
            ),
            Monkey(
                3, [74], Monkey.POSSIBLE_OPERATORS["+"], "3", 17, {True: 0, False: 1}
            ),
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
