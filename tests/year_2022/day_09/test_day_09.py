"""Tests for Day9 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2022.day_09.day_09 import (
    Day9,
    Down,
    Instruction,
    Left,
    Right,
    Up,
)
from tests.year_2022.abstract_test_day_2022 import AbstractTestDay2022


class TestDay(AbstractTestDay2022):
    """Test class for testing day 9."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 9

    @staticmethod
    def solver() -> type[Day9]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day9

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (
                1,
                (
                    Instruction(direction=Right, num_steps=4),
                    Instruction(direction=Up, num_steps=4),
                    Instruction(direction=Left, num_steps=3),
                    Instruction(direction=Down, num_steps=1),
                    Instruction(direction=Right, num_steps=4),
                    Instruction(direction=Down, num_steps=1),
                    Instruction(direction=Left, num_steps=5),
                    Instruction(direction=Right, num_steps=2),
                ),
            ),
            (
                2,
                (
                    Instruction(direction=Right, num_steps=5),
                    Instruction(direction=Up, num_steps=8),
                    Instruction(direction=Left, num_steps=8),
                    Instruction(direction=Down, num_steps=3),
                    Instruction(direction=Right, num_steps=17),
                    Instruction(direction=Down, num_steps=10),
                    Instruction(direction=Left, num_steps=25),
                    Instruction(direction=Up, num_steps=20),
                ),
            ),
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
        "example, result", ((1, 13), (2, 88)), indirect=["example"]
    )
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize("example, result", ((1, 1), (2, 36)), indirect=["example"])
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
