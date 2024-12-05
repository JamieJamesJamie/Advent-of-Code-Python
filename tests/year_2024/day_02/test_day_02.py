"""Tests for Day2 Solution class."""

import pytest

from advent_of_code.year_2024.day_02.day_02 import Day2
from tests.year_2024.abstract_test_day_2024 import AbstractTestDay2024


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2024):
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

        :return: The solver class that is being tested.
        """
        return Day2

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert tuple(example) == (
            (7, 6, 4, 2, 1),
            (1, 2, 7, 8, 9),
            (9, 7, 6, 2, 1),
            (1, 3, 2, 4, 5),
            (8, 6, 4, 4, 1),
            (1, 3, 6, 7, 9),
        )

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 2

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 4
