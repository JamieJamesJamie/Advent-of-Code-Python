"""Solutions for day 6."""

from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum
from typing import NamedTuple

import numpy as np
import parse as external_parse

from advent_of_code.helper.solver import Solver


class Action(StrEnum):
    """An action to perform on a set of lights."""

    TURN_ON = "turn on"
    TURN_OFF = "turn off"
    TOGGLE = "toggle"


class LineParserKey(StrEnum):
    """The keys to use to parse instructions."""

    ACTION = "action"
    COORD_1_X = "coord_1_x"
    COORD_1_Y = "coord_1_y"
    COORD_2_X = "coord_2_x"
    COORD_2_Y = "coord_2_y"


class Coordinate(NamedTuple):
    """Coordinate of a light."""

    x: int
    y: int


@dataclass
class Instruction:
    """An instruction to perform on a set of lights."""

    action: Action
    coordinate1: Coordinate
    coordinate2: Coordinate


class Day6(Solver):
    """Solver for day 6."""

    INSTRUCTION_PATTERN = external_parse.compile(
        f"{{{LineParserKey.ACTION}}} "
        f"{{{LineParserKey.COORD_1_X}:d}},{{{LineParserKey.COORD_1_Y}:d}}"
        " through "
        f"{{{LineParserKey.COORD_2_X}:d}},{{{LineParserKey.COORD_2_Y}:d}}"
    )

    @staticmethod
    def _parse_line(line: str):
        """Parses a single line of instruction.

        :param line: The instruction to parse.
        :return: The parsed instruction.
        """
        result = Day6.INSTRUCTION_PATTERN.parse(line)
        return Instruction(
            result[LineParserKey.ACTION],
            Coordinate(
                result[LineParserKey.COORD_1_X], result[LineParserKey.COORD_1_Y]
            ),
            Coordinate(
                result[LineParserKey.COORD_2_X], result[LineParserKey.COORD_2_Y]
            ),
        )

    @staticmethod
    def _map_action_part_1(action: Action, light_slice):
        """Returns the adjusted lights after performing the given
        :param:action.

        :param action: The action to perform.
        :param light_slice: The lights to perform the action on.
        :return: The adjusted lights after performing the given action.
        """
        match action:
            case Action.TOGGLE:
                return ~light_slice
            case Action.TURN_ON:
                return True
            case Action.TURN_OFF:
                return False
            case _:
                raise NotImplementedError()

    @staticmethod
    def _map_action_part_2(action: Action, light_slice):
        """Returns the adjusted lights after performing the given
        :param:action.

        :param action: The action to perform.
        :param light_slice: The lights to perform the action on.
        :return: The adjusted lights after performing the given action.
        """
        match action:
            case Action.TOGGLE:
                return light_slice + 2
            case Action.TURN_ON:
                return light_slice + 1
            case Action.TURN_OFF:
                return np.maximum(light_slice - 1, 0)
            case _:
                raise NotImplementedError()

    @staticmethod
    def _calculate_light_sum(instructions: Iterable[Instruction], dtype, mapper) -> int:
        """Calculates the brightness of the lights after following the
        :param:`instructions`.

        :param instructions: The instructions to follow.
        :param dtype: The type of light brightness.
        :param mapper: The mapper to use to adjust the lights'
            brightness.
        :return: The total brightness of the lights after following the
            given instructions.
        """
        lights = np.zeros((1000, 1000), dtype=dtype)

        for instruction in instructions:
            lights[
                instruction.coordinate1.x : instruction.coordinate2.x + 1,
                instruction.coordinate1.y : instruction.coordinate2.y + 1,
            ] = mapper(
                instruction.action,
                lights[
                    instruction.coordinate1.x : instruction.coordinate2.x + 1,
                    instruction.coordinate1.y : instruction.coordinate2.y + 1,
                ],
            )

        return lights.sum()

    @staticmethod
    def parse(puzzle_input: str) -> Iterable[Instruction]:
        """Parse input for puzzle 6.

        :param puzzle_input: Input to parse.
        :return: The instructions for the ideal lighting configuration.
        """
        return (Day6._parse_line(line) for line in puzzle_input.splitlines())

    @staticmethod
    def part1(parsed_input: Iterable[Instruction]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The number of lights that are lit after following the
            given instructions.
        """
        return Day6._calculate_light_sum(parsed_input, bool, Day6._map_action_part_1)

    @staticmethod
    def part2(parsed_input: Iterable[Instruction]) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The total brightness of the lights after following the
            given instructions.
        """
        return Day6._calculate_light_sum(parsed_input, int, Day6._map_action_part_2)
