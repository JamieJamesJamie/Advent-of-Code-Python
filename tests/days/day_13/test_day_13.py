"""Tests for Day13 Solution class."""


import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_13.day_13 import Day13


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay13(AbstractTestDay):
    """Test class for testing day 13."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 13

    @staticmethod
    def solver() -> type[Day13]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day13

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == (
            ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
            ([[1], [2, 3, 4]], [[1], 4]),
            ([9], [[8, 7, 6]]),
            ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
            ([7, 7, 7, 7], [7, 7, 7]),
            ([], [3]),
            ([[[]]], [[]]),
            ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
        )

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 13

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 140
