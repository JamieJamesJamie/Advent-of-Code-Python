"""Tests for Day14 Solution class."""


import pytest

from advent_of_code.year_2022.day_14.day_14 import Day14, Element, Position
from tests.year_2022.abstract_test_day_2022 import AbstractTestDay2022


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2022):
    """Test class for testing day 14."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 14

    @staticmethod
    def solver() -> type[Day14]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day14

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example == {
            Position(x=494, y=9): Element.ROCK,
            Position(x=495, y=9): Element.ROCK,
            Position(x=496, y=6): Element.ROCK,
            Position(x=496, y=9): Element.ROCK,
            Position(x=497, y=6): Element.ROCK,
            Position(x=497, y=9): Element.ROCK,
            Position(x=498, y=4): Element.ROCK,
            Position(x=498, y=5): Element.ROCK,
            Position(x=498, y=6): Element.ROCK,
            Position(x=498, y=9): Element.ROCK,
            Position(x=499, y=9): Element.ROCK,
            Position(x=500, y=9): Element.ROCK,
            Position(x=501, y=9): Element.ROCK,
            Position(x=502, y=4): Element.ROCK,
            Position(x=502, y=5): Element.ROCK,
            Position(x=502, y=6): Element.ROCK,
            Position(x=502, y=7): Element.ROCK,
            Position(x=502, y=8): Element.ROCK,
            Position(x=502, y=9): Element.ROCK,
            Position(x=503, y=4): Element.ROCK,
        }

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 24

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 93
