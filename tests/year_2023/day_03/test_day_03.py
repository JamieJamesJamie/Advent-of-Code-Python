"""Tests for Day3 Solution class."""

import numpy as np
import pytest

from advent_of_code.year_2023.day_03.day_03 import Day3, ParsedInput
from tests.year_2023.abstract_test_day_2023 import AbstractTestDay2023


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2023):
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

    def test_parse_example(self, example: ParsedInput):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert (
            example.character_map
            == np.array(
                (
                    ("4", "6", "7", ".", ".", "1", "1", "4", ".", "."),
                    (".", ".", ".", "*", ".", ".", ".", ".", ".", "."),
                    (".", ".", "3", "5", ".", ".", "6", "3", "3", "."),
                    (".", ".", ".", ".", ".", ".", "#", ".", ".", "."),
                    ("6", "1", "7", "*", ".", ".", ".", ".", ".", "."),
                    (".", ".", ".", ".", ".", "+", ".", "5", "8", "."),
                    (".", ".", "5", "9", "2", ".", ".", ".", ".", "."),
                    (".", ".", ".", ".", ".", ".", "7", "5", "5", "."),
                    (".", ".", ".", "$", ".", "*", ".", ".", ".", "."),
                    (".", "6", "6", "4", ".", "5", "9", "8", ".", "."),
                )
            )
        ).all()

        assert example.numbers == (
            ((467, (0, 2)), (114, (5, 7))),
            (),
            ((35, (2, 3)), (633, (6, 8))),
            (),
            ((617, (0, 2)),),
            ((58, (7, 8)),),
            ((592, (2, 4)),),
            ((755, (6, 8)),),
            (),
            ((664, (1, 3)), (598, (5, 7))),
        )

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 4_361

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 467_835
