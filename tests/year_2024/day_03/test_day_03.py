"""Tests for Day3 Solution class."""

# pylint: disable=arguments-differ,R0801


import pytest

from advent_of_code.year_2024.day_03.day_03 import Day3
from tests.year_2024.abstract_test_day_2024 import AbstractTestDay2024


class TestDay(AbstractTestDay2024):
    """Test class for testing day 3."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 3

    @staticmethod
    def solver() -> type[Day3]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day3

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, "mul(44,46)"),
            (2, "mul(123,4)"),
            (3, "mul(4*"),
            (4, "mul(6,9!"),
            (5, "?(12,34)"),
            (6, "mul ( 2 , 4 )"),
            (
                7,
                "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+"
                "mul(32,64]then(mul(11,8)mul(8,5))",
            ),
            (
                8,
                "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+"
                "mul(32,64](mul(11,8)undo()?mul(8,5))",
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
        "example, result",
        ((1, 2024), (2, 492), (3, 0), (4, 0), (5, 0), (6, 0), (7, 161), (8, 161)),
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
        ((1, 2024), (2, 492), (3, 0), (4, 0), (5, 0), (6, 0), (7, 161), (8, 48)),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
