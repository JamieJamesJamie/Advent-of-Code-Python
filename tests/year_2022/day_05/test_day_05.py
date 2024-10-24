"""Tests for Day5 Solution class."""

import pytest

from advent_of_code.year_2022.day_05.day_05 import Day5, Instruction
from tests.year_2022.abstract_test_day_2022 import AbstractTestDay2022


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2022):
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

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example.instructions == (
            Instruction(num_to_move=1, from_crate="2", to_crate="1"),
            Instruction(num_to_move=3, from_crate="1", to_crate="3"),
            Instruction(num_to_move=2, from_crate="2", to_crate="1"),
            Instruction(num_to_move=1, from_crate="1", to_crate="2"),
        )
        assert example.stacks == {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == "CMZ"

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == "MCD"
