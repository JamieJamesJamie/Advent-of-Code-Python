"""Tests for Day4 Solution class."""

import numpy as np
import pytest

from advent_of_code.year_2024.day_04.day_04 import Day4
from tests.year_2024.abstract_test_day_2024 import AbstractTestDay2024


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2024):
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

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert (
            example
            == np.array(
                (
                    ("M", "M", "M", "S", "X", "X", "M", "A", "S", "M"),
                    ("M", "S", "A", "M", "X", "M", "S", "M", "S", "A"),
                    ("A", "M", "X", "S", "X", "M", "A", "A", "M", "M"),
                    ("M", "S", "A", "M", "A", "S", "M", "S", "M", "X"),
                    ("X", "M", "A", "S", "A", "M", "X", "A", "M", "M"),
                    ("X", "X", "A", "M", "M", "X", "X", "A", "M", "A"),
                    ("S", "M", "S", "M", "S", "A", "S", "X", "S", "S"),
                    ("S", "A", "X", "A", "M", "A", "S", "A", "A", "A"),
                    ("M", "A", "M", "M", "M", "X", "M", "M", "M", "M"),
                    ("M", "X", "M", "X", "A", "X", "M", "A", "S", "X"),
                )
            )
        ).all()

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 18

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 9
