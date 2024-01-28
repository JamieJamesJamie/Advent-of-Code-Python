"""Utility functions to download puzzle input."""

from pathlib import Path

from aocd.models import Puzzle

from advent_of_code.helper.paths import puzzle_inputs_path, year_day_path


def download(output_path: Path, year: int, day: int):
    """Downloads puzzle data to the specified path.

    If file_name starts with "input", then the puzzle input is
    downloaded and written to the file. Otherwise, the example input is
    downloaded and written to the file.

    :param output_path: Path of the file to write to.
    :param year: Year to download puzzle input from.
    :param day: Day to download and write puzzle input from and to
        respectively.
    """

    puzzle = Puzzle(year=year, day=day)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not output_path.is_file():
        output_path.write_text(
            (
                puzzle.input_data
                if output_path.stem.startswith("input")
                else puzzle.example_data
            )
            + "\n"
        )


def read_file(input_file: Path, year: int, day: int) -> str:
    """Reads puzzle data from the specified input file.

    If the path doesn't exist, then the data is downloaded.

    :param input_file: Path of the file to read from.
    :param year: Year to get puzzle input from.
    :param day: Day to get puzzle input for.
    :return: The puzzle input.
    """
    input_path = puzzle_inputs_path() / year_day_path(year=year, day=day) / input_file

    if not input_path.exists():
        download(output_path=input_path, year=year, day=day)

    return "\n".join(
        line.rstrip() for line in input_path.read_text().splitlines()
    ).rstrip()
