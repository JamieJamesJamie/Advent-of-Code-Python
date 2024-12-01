"""Tests for Day1 Solution class."""

import pytest

from advent_of_code.year_2024.day_01.day_01 import Day1
from tests.year_2024.abstract_test_day_2024 import AbstractTestDay2024


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2024):
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

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert tuple(example) == ((3, 4, 2, 1, 3, 3), (4, 3, 5, 3, 9, 3))

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 11

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 31
