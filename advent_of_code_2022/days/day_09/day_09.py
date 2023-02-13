"""Solutions for day 9."""


# pylint: disable=too-few-public-methods


from abc import ABC, abstractmethod
from typing import NamedTuple

import numpy as np

from advent_of_code_2022.helper.solver import Solver


class Position(NamedTuple):
    """The position of a knot in the rope."""

    x: int
    y: int

    def is_touching(self, position: "Position") -> bool:
        """Returns whether this knot is touching the :param:`position` of
        another knot.

        :param position: The position of another knot.
        :return: Whether this knot and the given knot are touching.
        """
        return (
            # Same position
            self == position
            # position is directly above or below self
            or (self.x == position.x and abs(self.y - position.y) == 1)
            # position is directly left or right of self
            or (self.y == position.y and abs(self.x - position.x) == 1)
            # position is directly diagonal of self
            or (abs(self.x - position.x) == 1 and abs(self.y - position.y) == 1)
        )

    def distance_from(self, position: "Position") -> int:
        """Returns the distance between this knot's position and the
        :param:`position` of another knot.

        :param position: The position of another knot.
        :return: The distance between this knot and another knot.
        """
        return abs(self.x - position.x) + abs(self.y - position.y)


class SolverState:
    """The state of the solver."""

    def __init__(self, rope_length: int):
        """The constructor for the :class:`SolverState`.

        :param rope_length: The length of the rope being used in the puzzle.
        """
        self.current_positions = [Position(0, 0) for _ in range(rope_length)]
        self.all_tail_positions = {self.current_positions[-1]}


class Direction(ABC):
    """A direction."""

    @classmethod
    def compute(cls, num_steps: int, solver_state: SolverState) -> SolverState:
        """Computes the positions of each knot in the rope and what positions
        the tail of the rope has traversed.

        :param num_steps: Number of steps to traverse the head of the rope.
        :param solver_state: Current state of the solver.
        :return: The new state of the solver.
        """
        for _ in range(num_steps):
            solver_state.current_positions[0] = cls._move_one_step(
                solver_state.current_positions[0]
            )

            for knot_index, (knot_pos_1, knot_pos_2) in enumerate(
                zip(solver_state.current_positions, solver_state.current_positions[1:])
            ):
                if knot_pos_1.is_touching(knot_pos_2):
                    # This knot isn't going to move,
                    # so subsequent knots aren't going to move
                    break

                solver_state.current_positions[
                    knot_index + 1
                ] = cls._compute_new_tail_position(knot_pos_1, knot_pos_2)

            solver_state.all_tail_positions.add(solver_state.current_positions[-1])

            # Day9.print_map(solver_state)

        return solver_state

    @staticmethod
    def _compute_new_tail_position(
        head_position: Position, tail_position: Position
    ) -> Position:
        distance = head_position.distance_from(tail_position)

        if head_position.x == tail_position.x and distance == 2:
            return Position(
                tail_position.x,
                tail_position.y + (1 if head_position.y > tail_position.y else -1),
            )

        if head_position.y == tail_position.y and distance == 2:
            return Position(
                tail_position.x + (1 if head_position.x > tail_position.x else -1),
                tail_position.y,
            )

        return Position(
            tail_position.x + (1 if head_position.x > tail_position.x else -1),
            tail_position.y + (1 if head_position.y > tail_position.y else -1),
        )

    @staticmethod
    @abstractmethod
    def _move_one_step(position: Position) -> Position:
        """
        Returns a new position one step in a particular direction away from
        :param:`position`.

        :param position: The position of a knot.
        :return: A new position one step in a particular direction away from the given
            position.
        """


class Up(Direction):
    """The up direction."""

    @staticmethod
    def _move_one_step(position: Position) -> Position:
        """Returns a new position one step up away from :param:`position`.

        :param position: The position of a knot.
        :return: A new position one step up away from the given position.
        """
        return Position(position.x, position.y + 1)


class Down(Direction):
    """The down direction."""

    @staticmethod
    def _move_one_step(position: Position) -> Position:
        """Returns a new position one step down away from :param:`position`.

        :param position: The position of a knot.
        :return: A new position one step down away from the given position.
        """
        return Position(position.x, position.y - 1)


class Left(Direction):
    """The left direction."""

    @staticmethod
    def _move_one_step(position: Position) -> Position:
        """Returns a new position one step left away from :param:`position`.

        :param position: The position of a knot.
        :return: A new position one step left away from the given position.
        """
        return Position(position.x - 1, position.y)


class Right(Direction):
    """The right direction."""

    @staticmethod
    def _move_one_step(position: Position) -> Position:
        """Returns a new position one step right away from :param:`position`.

        :param position: The position of a knot.
        :return: A new position one step right away from the given position.
        """
        return Position(position.x + 1, position.y)


class Instruction(NamedTuple):
    """An instruction from the puzzle input."""

    direction: type[Direction]
    num_steps: int


class Day9(Solver):
    """Solver for day 9."""

    _START_POSITION = Position(0, 0)
    _MOVE: dict[str, type[Direction]] = {"U": Up, "D": Down, "L": Left, "R": Right}

    @staticmethod
    def generate_map(solver_state: SolverState) -> np.ndarray:
        """Returns the current state of the map.

        :param solver_state: Current state of the solver.
        :return: The current state of the map.
        """
        min_position = Position(
            min(
                *(position.x for position in solver_state.current_positions),
                *(position.x for position in solver_state.all_tail_positions),
            ),
            min(
                *(position.y for position in solver_state.current_positions),
                *(position.y for position in solver_state.all_tail_positions),
            ),
        )
        max_position = Position(
            max(
                *(position.x for position in solver_state.current_positions),
                *(position.x for position in solver_state.all_tail_positions),
            ),
            max(
                *(position.y for position in solver_state.current_positions),
                *(position.y for position in solver_state.all_tail_positions),
            ),
        )

        map_to_print = np.array(
            [
                ["." for _ in range(min_position.y, max_position.y + 1)]
                for _ in range(min_position.x, max_position.x + 1)
            ]
        )

        for recorded_tail_position in solver_state.all_tail_positions:
            map_to_print[
                recorded_tail_position.x - min_position.x,
                recorded_tail_position.y - min_position.y,
            ] = "#"

        map_to_print[
            Day9._START_POSITION.x - min_position.x,
            Day9._START_POSITION.y - min_position.y,
        ] = "s"

        for rope_index, rope_position in reversed(
            tuple(enumerate(solver_state.current_positions))
        ):
            map_to_print[
                rope_position.x - min_position.x, rope_position.y - min_position.y
            ] = ("H" if rope_index == 0 else str(rope_index))

        map_to_print = np.rot90(map_to_print)

        return map_to_print

    @staticmethod
    def print_map(solver_state: SolverState) -> None:
        """Prints the current state of the map.

        :param solver_state: Current state of the solver.
        """
        map_to_print = Day9.generate_map(solver_state)

        for row in map_to_print:
            print("".join(row))

        print()

    @staticmethod
    def parse(puzzle_input: str) -> tuple[Instruction, ...]:
        """Parse input for puzzle 9.

        :param puzzle_input: Input to parse.
        :return: A sequence of instructions to move the head of the rope.
        """
        instructions = []

        for line in puzzle_input.split("\n"):
            direction, num_steps = line.split()
            instructions.append(
                Instruction(
                    Day9._MOVE[direction],
                    int(num_steps),
                )
            )

        return tuple(instructions)

    @staticmethod
    def _solve_puzzle(instructions: tuple[Instruction, ...], rope_length: int) -> int:
        """Solves the puzzle.

        :param instructions: A sequence of instructions to move the head of the rope.
        :param rope_length: The length of the rope being used in the puzzle.
        :return: The number of positions the tail visited at least once.
        """
        solver_state = SolverState(rope_length=rope_length)

        for instruction in instructions:
            instruction.direction.compute(instruction.num_steps, solver_state)

        # Day9.print_map(solver_state)

        return len(solver_state.all_tail_positions)

    @staticmethod
    def part1(parsed_input: tuple[Instruction, ...]) -> int:
        """Solves part 1.

        :param parsed_input: A sequence of instructions to move the head of the rope.
        :return: The number of positions the tail visited at least once.
        """
        return Day9._solve_puzzle(instructions=parsed_input, rope_length=2)

    @staticmethod
    def part2(parsed_input: tuple[Instruction, ...]) -> int:
        """Solves part 2.

        :param parsed_input: A sequence of instructions to move the head of the rope.
        :return: The number of positions the tail visited at least once.
        """
        return Day9._solve_puzzle(instructions=parsed_input, rope_length=10)
