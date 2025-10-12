"""Utility functions to parse command line arguments."""

# pylint: disable=too-few-public-methods


from pathlib import Path

from tap import Tap

DEFAULT_FILE_PATH = Path("input.txt")


class ArgumentParser(Tap):
    """Typed Argument Parser (TAP) class used to parse command line arguments
    into the program."""

    years: tuple[int, ...]
    """Years of the puzzles to solve."""

    days: tuple[int, ...]
    """Days of the puzzles to solve."""

    files: tuple[Path, ...] = (DEFAULT_FILE_PATH,)
    """Sequence of file paths to run the puzzle with."""

    def configure(self) -> None:
        # pylint: disable=attribute-defined-outside-init,missing-function-docstring

        self.description = "My Advent of Code solutions."
