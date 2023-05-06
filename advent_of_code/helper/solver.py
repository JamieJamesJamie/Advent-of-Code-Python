"""Utilities to create solutions in a consistent way."""

from abc import ABC, abstractmethod
from typing import Any


class Solver(ABC):
    """Abstract Base Class to solve Advent of Code puzzles."""

    @staticmethod
    @abstractmethod
    def parse(puzzle_input: str) -> Any:
        """Parses input.

        :param puzzle_input: Input to parse.
        :return: The parsed input.
        """

    @staticmethod
    @abstractmethod
    def part1(parsed_input: Any) -> Any:
        """Solves part 1.

        :param parsed_input: The parsed input.
        :return: A solution to part 1.
        """

    @staticmethod
    @abstractmethod
    def part2(parsed_input: Any) -> Any:
        """Solves part 2.

        :param parsed_input: The parsed input.
        :return: A solution to part 2.
        """
