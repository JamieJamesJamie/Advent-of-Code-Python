"""Utility functions that provide common paths."""


from pathlib import Path


def puzzle_inputs_path() -> Path:
    """
    Returns the :class:`Path` of the puzzle inputs directory.

    :return: The Path of the puzzle inputs directory.
    """
    return Path(__file__).parents[2] / "puzzle_inputs"


def year_day_path(year: int, day: int) -> Path:
    """
    Returns the directory to use for the specified day.

    :param year: The year to get the directory for.
    :param day: The day to get the directory for.
    :return: The directory that should be used for the specified day.
    """
    return Path(f"year_{year:04d}") / f"day_{day:02d}"


def src_path() -> Path:
    """
    Returns the :class:`Path` of the directory where the year subdirectories are
    located.

    :return: The Path of the directory where the year subdirectories are located.
    """
    return Path(__file__).parents[1]
