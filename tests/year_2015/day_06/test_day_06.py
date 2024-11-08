"""Tests for Day6 Solution class."""

# pylint: disable=arguments-differ


import pytest

from advent_of_code.year_2015.day_06.day_06 import Action, Coordinate, Day6, Instruction
from tests.year_2015.abstract_test_day_2015 import AbstractTestDay2015


class TestDay(AbstractTestDay2015):
    """Test class for testing day 6."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 6

    @staticmethod
    def solver() -> type[Day6]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day6

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, (Instruction(Action.TURN_ON, Coordinate(0, 0), Coordinate(999, 999)),)),
            (2, (Instruction(Action.TOGGLE, Coordinate(0, 0), Coordinate(999, 0)),)),
            (
                3,
                (
                    Instruction(
                        Action.TURN_OFF, Coordinate(499, 499), Coordinate(500, 500)
                    ),
                ),
            ),
            (
                4,
                (
                    Instruction(Action.TURN_ON, Coordinate(0, 0), Coordinate(999, 999)),
                    Instruction(Action.TOGGLE, Coordinate(0, 0), Coordinate(999, 0)),
                    Instruction(
                        Action.TURN_OFF, Coordinate(499, 499), Coordinate(500, 500)
                    ),
                ),
            ),
            (5, (Instruction(Action.TURN_ON, Coordinate(0, 0), Coordinate(0, 0)),)),
            (6, (Instruction(Action.TOGGLE, Coordinate(0, 0), Coordinate(999, 999)),)),
        ),
        indirect=["example"],
    )
    def test_parse_example(self, example, parsed):
        """Test that example input is parsed correctly.

        :param example: The actual parsed input from example file.
        :param parsed: The expected parsed input from example file.
        """
        assert tuple(example) == parsed

    @pytest.mark.parametrize(
        "example, result",
        ((1, 1_000_000), (2, 1000), (3, 0), (4, 998_996), (5, 1), (6, 1_000_000)),
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
        ((1, 1_000_000), (2, 2000), (3, 0), (4, 1_001_996), (5, 1), (6, 2_000_000)),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
