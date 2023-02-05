"""Tests for Day2 Solution class."""
import pytest
from days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_02.day_02 import Day2


@pytest.mark.usefixtures("example1")
class TestDay2(AbstractTestDay):
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

    def test_parse_example1(self, example1):
        """Test that example1 input is parsed correctly.

        :param example1: Parsed input from example1 file.
        """
        assert example1 == (("A", "Y"), ("B", "X"), ("C", "Z"))

    def test_part1_example1(self, example1):
        """Test part 1 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part1(example1) == 15

    def test_part2_example1(self, example1):
        """Test part 2 on example1 input.

        :param example1: Parsed input from example1 file.
        """
        assert self.solver().part2(example1) == 12
