"""Tests for Day10 Solution class."""





# pylint: disable=arguments-differ




import os

import pytest
from tests.days.helper.abstract_test_day import AbstractTestDay

from advent_of_code_2022.days.day_10.day_10 import Day10


class TestDay10(AbstractTestDay):
    """Test class for testing day 10."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 10

    @staticmethod
    def solver() -> type[Day10]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day10

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, (("noop",), ("addx", "3"), ("addx", "-5"))),
            (
                2,
                (
                    ("addx", "15"),
                    ("addx", "-11"),
                    ("addx", "6"),
                    ("addx", "-3"),
                    ("addx", "5"),
                    ("addx", "-1"),
                    ("addx", "-8"),
                    ("addx", "13"),
                    ("addx", "4"),
                    ("noop",),
                    ("addx", "-1"),
                    ("addx", "5"),
                    ("addx", "-1"),
                    ("addx", "5"),
                    ("addx", "-1"),
                    ("addx", "5"),
                    ("addx", "-1"),
                    ("addx", "5"),
                    ("addx", "-1"),
                    ("addx", "-35"),
                    ("addx", "1"),
                    ("addx", "24"),
                    ("addx", "-19"),
                    ("addx", "1"),
                    ("addx", "16"),
                    ("addx", "-11"),
                    ("noop",),
                    ("noop",),
                    ("addx", "21"),
                    ("addx", "-15"),
                    ("noop",),
                    ("noop",),
                    ("addx", "-3"),
                    ("addx", "9"),
                    ("addx", "1"),
                    ("addx", "-3"),
                    ("addx", "8"),
                    ("addx", "1"),
                    ("addx", "5"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "-36"),
                    ("noop",),
                    ("addx", "1"),
                    ("addx", "7"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "2"),
                    ("addx", "6"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "1"),
                    ("noop",),
                    ("noop",),
                    ("addx", "7"),
                    ("addx", "1"),
                    ("noop",),
                    ("addx", "-13"),
                    ("addx", "13"),
                    ("addx", "7"),
                    ("noop",),
                    ("addx", "1"),
                    ("addx", "-33"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "2"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "8"),
                    ("noop",),
                    ("addx", "-1"),
                    ("addx", "2"),
                    ("addx", "1"),
                    ("noop",),
                    ("addx", "17"),
                    ("addx", "-9"),
                    ("addx", "1"),
                    ("addx", "1"),
                    ("addx", "-3"),
                    ("addx", "11"),
                    ("noop",),
                    ("noop",),
                    ("addx", "1"),
                    ("noop",),
                    ("addx", "1"),
                    ("noop",),
                    ("noop",),
                    ("addx", "-13"),
                    ("addx", "-19"),
                    ("addx", "1"),
                    ("addx", "3"),
                    ("addx", "26"),
                    ("addx", "-30"),
                    ("addx", "12"),
                    ("addx", "-1"),
                    ("addx", "3"),
                    ("addx", "1"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "-9"),
                    ("addx", "18"),
                    ("addx", "1"),
                    ("addx", "2"),
                    ("noop",),
                    ("noop",),
                    ("addx", "9"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
                    ("addx", "-1"),
                    ("addx", "2"),
                    ("addx", "-37"),
                    ("addx", "1"),
                    ("addx", "3"),
                    ("noop",),
                    ("addx", "15"),
                    ("addx", "-21"),
                    ("addx", "22"),
                    ("addx", "-6"),
                    ("addx", "1"),
                    ("noop",),
                    ("addx", "2"),
                    ("addx", "1"),
                    ("noop",),
                    ("addx", "-10"),
                    ("noop",),
                    ("noop",),
                    ("addx", "20"),
                    ("addx", "1"),
                    ("addx", "2"),
                    ("addx", "2"),
                    ("addx", "-6"),
                    ("addx", "-11"),
                    ("noop",),
                    ("noop",),
                    ("noop",),
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
        assert tuple(example) == tuple(parsed)

    @pytest.mark.parametrize(
        "example, result",
        (
            (1, 0),
            (2, 13_140),
        ),
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
        (
            (
                1,
                os.linesep.join(
                    """#####.
#
#
#
#
#""".split()
                ),
            ),
            (
                2,
                os.linesep.join(
                    """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""".split()
                ),
            ),
        ),
        indirect=["example"],
    )
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
