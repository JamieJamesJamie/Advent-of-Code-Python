"""Utility functions to download puzzle input."""

from pathlib import Path

from aocd.models import Puzzle


def directory_path(day: int) -> Path:
    """Returns the directory to use for the specified day.

    :param day: The day to get the directory for.
    :return: The directory that should be used for the specified day.
    """
    return Path(__file__).parents[1] / "days" / f"day_{day:02d}"


def download(output_path: Path, day: int, year: int = 2022):
    """Downloads puzzle data to the specified path.

    If file_name starts with "input",
    then the puzzle input is downloaded and written to the file.
    Otherwise, the example input is downloaded and written to the file.

    :param output_path: Path of the file to write to.
    :param day: Day to download and write puzzle input from and to respectively.
    :param year: Year to download puzzle input from.
    """

    puzzle = Puzzle(year=year, day=day)

    if not output_path.is_file():
        output_path.write_text(
            (
                puzzle.input_data
                if output_path.stem.startswith("input")
                else puzzle.example_data
            )
            + "\n"
        )


def read_file(input_path: Path, day: int, year: int = 2022) -> str:
    """Reads puzzle data from the specified path. If the path doesn't exist,
    then the data is downloaded.

    :param input_path: Path of the file to read from.
    :param day: Day to get puzzle input for.
    :param year: Year to get puzzle input from.
    :return: The puzzle input.
    """

    if not input_path.exists():
        download(output_path=input_path, day=day, year=year)

    return "\n".join(
        line.rstrip() for line in input_path.read_text().split("\n")
    ).rstrip()
