"""Solutions for day 3."""

import math
import re
from collections.abc import Iterator

from parse import compile as external_compile

from advent_of_code.helper.solver import Solver


class Day3(Solver):
    """Solver for day 3."""

    MUL_PARSER = external_compile("mul({:3d},{:3d})")
    MUL_REGEX = r"mul\(\d{1,3},\d{1,3}\)"

    @staticmethod
    def _iterate_through_parsed_enabled_input(parsed_input: str) -> Iterator[int]:
        enabled = True
        for match in re.finditer(rf"{Day3.MUL_REGEX}|do\(\)|don't\(\)", parsed_input):
            match_string = match.group()

            if match_string == "do()":
                enabled = True
            elif match_string == "don't()":
                enabled = False
            elif enabled:
                yield math.prod(
                    int(term) for term in Day3.MUL_PARSER.parse(match_string)
                )

    @staticmethod
    def parse(puzzle_input: str) -> str:
        """Parse input for puzzle 3.

        :param puzzle_input: Input to parse.
        :return: The parsed input.
        """
        return puzzle_input

    @staticmethod
    def part1(parsed_input: str) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The sum of the multiplications.
        """
        return sum(
            math.prod(int(term) for term in terms)
            for terms in Day3.MUL_PARSER.findall(parsed_input)
        )

    @staticmethod
    def part2(parsed_input: str) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The sum of the enabled multiplications.
        """
        return sum(Day3._iterate_through_parsed_enabled_input(parsed_input))
