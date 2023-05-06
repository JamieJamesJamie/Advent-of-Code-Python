"""Module to solve Advent of Code puzzles from."""


from pathlib import Path

from advent_of_code.helper.download_files import read_file
from advent_of_code.helper.solver import Solver


def solve(input_path: Path, day: int, year: int) -> tuple[str, str]:
    """
    Solves the specified :param:`day`'s problem using the input specified in
    :param:`input_path`.

    :param input_path: The path to read the input from.
    :param day: The day the problem was released.
    :param year: The year the problem was released.
    :return: The solutions for part 1 and part 2 respectively to the specified problem.
    """
    puzzle_input = read_file(input_path=input_path, year=year, day=day)

    solver_name = f"Day{day}"
    solver_module = __import__(
        ".".join(input_path.with_name(input_path.parts[-2]).parts[-4:]),
        fromlist=[solver_name],
    )
    solver: Solver = getattr(solver_module, solver_name)

    part1_solution = solver.part1(solver.parse(puzzle_input))
    part2_solution = solver.part2(solver.parse(puzzle_input))

    return str(part1_solution), str(part2_solution)
