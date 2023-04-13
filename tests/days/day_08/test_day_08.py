"""Tests for Day8 Solution class."""






import numpy as np
import pytest
from tests.days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_08.day_08 import Day8


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay8(AbstractTestDay):
    """Test class for testing day 8."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 8

    @staticmethod
    def solver() -> type[Day8]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day8

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert (
            example
            == np.array(
                [
                    [3, 0, 3, 7, 3],
                    [2, 5, 5, 1, 2],
                    [6, 5, 3, 3, 2],
                    [3, 3, 5, 4, 9],
                    [3, 5, 3, 9, 0],
                ],
                dtype=np.int8,
            )
        ).all()

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 21

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 8
