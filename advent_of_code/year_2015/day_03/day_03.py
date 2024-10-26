"""Solutions for day 3."""

import itertools

import numpy as np

from advent_of_code.helper.solver import Solver


class Day3(Solver):
    """Solver for day 3."""

    DIRECTION_MAPPINGS: dict[str, np.ndarray] = {
        "^": np.array((0, 1)),
        "v": np.array((0, -1)),
        ">": np.array((1, 0)),
        "<": np.array((-1, 0)),
    }

    @staticmethod
    def _traverse_and_add_house_visit(
        houses_visited: set[bytes], current_position: np.ndarray, direction: str
    ) -> None:
        """Traverses to the next position and adds the new position to
        :param:`houses_visited`.

        :param houses_visited: The set of houses to add the new position
            to.
        :param current_position: The current position to traverse from.
        :param direction: The direction to traverse to.
        """
        current_position += Day3.DIRECTION_MAPPINGS[direction]
        houses_visited.add(current_position.tobytes())

    @staticmethod
    def parse(puzzle_input: str) -> str:
        """Parse input for puzzle 3.

        :param puzzle_input: The input to parse
        :return: The directions to follow.
        """
        return puzzle_input

    @staticmethod
    def part1(parsed_input: str) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The number of houses that Santa visits.
        """
        current_position = np.array((0, 0))
        houses_visited = {current_position.tobytes()}

        for direction in parsed_input:
            Day3._traverse_and_add_house_visit(
                houses_visited, current_position, direction
            )

        return len(houses_visited)

    @staticmethod
    def part2(parsed_input: str) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The number of houses that Santa and Robo-Santa visit.
        """
        santa_position = np.array((0, 0))
        robo_santa_position = np.array((0, 0))
        houses_visited = {santa_position.tobytes()}

        for direction, position in zip(
            parsed_input, itertools.cycle((santa_position, robo_santa_position))
        ):
            Day3._traverse_and_add_house_visit(
                houses_visited,
                position,
                direction,
            )

        return len(houses_visited)
