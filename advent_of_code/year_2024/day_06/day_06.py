"""Solutions for day 6."""

from enum import Enum
from typing import Any, NamedTuple

from advent_of_code.helper.solver import Solver


class Position(NamedTuple):
    """Position."""

    x: int
    y: int


class GuardDirection(Enum):
    """Guard direction."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class ParsedInput:
    """Represents the parsed input."""

    # pylint: disable=too-few-public-methods

    def __init__(self, puzzle_input: str):
        self.obstructions = set()

        for y, line in enumerate(puzzle_input):
            self.max_height = y

            for x, character in enumerate(line):
                self.max_width = x

                if character == "#":
                    self.obstructions.add(Position(x, y))

                elif character == "^":
                    self.current_guard_position = Position(x, y)
                    self.guard_visited_positions = {self.current_guard_position}

        self.current_guard_direction = GuardDirection.UP

    def traverse_guard(self):
        """Idk yet.

        :return: Needs to be filled in.
        """


class Day6(Solver):
    """Solver for day 6."""

    @staticmethod
    def parse(puzzle_input: str) -> ParsedInput:
        return ParsedInput(puzzle_input)

    @staticmethod
    def part1(parsed_input: ParsedInput) -> int:
        while (
            0 <= parsed_input.current_guard_position.x < parsed_input.max_width
            and 0 <= parsed_input.current_guard_position.y < parsed_input.max_height
        ):
            return 7

        return 78

    @staticmethod
    def part2(parsed_input: ParsedInput) -> Any:
        pass
