"""Tests for Day1 Solution class."""




# pylint: disable=arguments-differ





import pytest





from advent_of_code.year_2023.day_01.day_01 import Day1
from tests.year_2023.abstract_test_day_2023 import AbstractTestDay2023






class TestDay(AbstractTestDay2023):
    """Test class for testing day 1."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 1

    @staticmethod
    def solver() -> type[Day1]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day1

    @pytest.mark.parametrize(
        "example, parsed",
        (
            (1, ("1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet")),
            (
                2,
                (
                    "two1nine",
                    "eightwothree",
                    "abcone2threexyz",
                    "xtwone3four",
                    "4nineeightseven2",
                    "zoneight234",
                    "7pqrstsixteen",
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

    @pytest.mark.parametrize("example, result", [[1, 142]], indirect=["example"])
    def test_part1_example(self, example, result):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part1(example) == result

    @pytest.mark.parametrize("example, result", [[2, 281]], indirect=["example"])
    def test_part2_example(self, example, result):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        :param result: The expected result.
        """
        assert self.solver().part2(example) == result
