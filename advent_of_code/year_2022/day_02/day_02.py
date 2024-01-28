"""Solutions for day 2."""

from collections.abc import Iterable
from enum import Enum
from typing import NamedTuple

from advent_of_code.helper.solver import Solver


class Move(Enum):
    """Score for the move that was played."""

    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(Enum):
    """Score for the outcome of the round."""

    WIN = 6
    LOSE = 0
    DRAW = 3


class RoundInfo(NamedTuple):
    """Information for a round of Rock Paper Scissors."""

    column1: str
    columns2: str


class Day2(Solver):
    """Solver for day 2."""

    _OPPONENT_TRANSLATIONS = {"A": Move.ROCK, "B": Move.PAPER, "C": Move.SCISSORS}

    @staticmethod
    def _outcome(opponent_move: Move, my_move: Move) -> Outcome:
        """Returns the :class:`Outcome` of a Rock Paper Scissors game, given
        the :param:`opponent_move` and :param:`my_move`.

        :param opponent_move: Opponent's move in Rock Paper Scissors.
        :param my_move: My move in Rock Paper Scissors.
        :return: The outcome of Rock Paper Scissors.
        """
        if my_move.value % len(Move) == opponent_move.value - 1:
            return Outcome.LOSE

        if my_move == opponent_move:
            return Outcome.DRAW

        return Outcome.WIN

    @staticmethod
    def _get_move(opponent_move: Move, my_outcome: Outcome) -> Move:
        """Returns the :class:`Move` that should be made in a Rock Paper
        Scissors game against the given :param:`opponent_move` to achieve the
        given :class:`my_outcome`.

        :param opponent_move: Opponent's move in Rock Paper Scissors.
        :param my_outcome: The outcome that should be achieved.
        :return: The move that should be made to achieve the given
            outcome.
        """
        if Day2._outcome(opponent_move, Move.ROCK) == my_outcome:
            return Move.ROCK

        if Day2._outcome(opponent_move, Move.PAPER) == my_outcome:
            return Move.PAPER

        return Move.SCISSORS

    @staticmethod
    def parse(puzzle_input: str) -> tuple[RoundInfo, ...]:
        """Parse input for puzzle 2.

        :param puzzle_input: Input to parse.
        :return: The columns (round info) for each round of Rock Paper
            Scissors.
        """
        return tuple(RoundInfo(*line.split(" ")) for line in puzzle_input.splitlines())

    @staticmethod
    def part1(parsed_input: Iterable[RoundInfo]) -> int:
        """Solves part 1.

        :param parsed_input: The round info for each round of Rock Paper
            Scissors.
        :return: The total score.
        """
        total_score = 0
        my_translations = {"X": Move.ROCK, "Y": Move.PAPER, "Z": Move.SCISSORS}

        for opponent_key, my_key in parsed_input:
            opponent_move = Day2._OPPONENT_TRANSLATIONS[opponent_key]
            my_move = my_translations[my_key]

            game_outcome = Day2._outcome(opponent_move, my_move).value
            move_outcome = my_move.value

            score = game_outcome + move_outcome
            total_score += score

        return total_score

    @staticmethod
    def part2(parsed_input: Iterable[RoundInfo]) -> int:
        """Solves part 2.

        :param parsed_input: The round info for each round of Rock Paper
            Scissors.
        :return: The total score.
        """
        total_score = 0
        my_translations = {"X": Outcome.LOSE, "Y": Outcome.DRAW, "Z": Outcome.WIN}

        for opponent_key, my_key in parsed_input:
            opponent_move = Day2._OPPONENT_TRANSLATIONS[opponent_key]
            my_outcome = my_translations[my_key]

            my_move = Day2._get_move(opponent_move, my_outcome)

            score = my_outcome.value + my_move.value
            total_score += score

        return total_score
