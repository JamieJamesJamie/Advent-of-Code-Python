"""Module to solve the Advent of Code puzzles from."""

from pathlib import Path

from advent_of_code.helper.download_files import read_file
from advent_of_code.helper.paths import src_path, year_day_path
from advent_of_code.helper.solver import Solver


def solve(input_file: Path, year: int, day: int) -> tuple[str, str]:
    """Solves the specified :param:`year`'s :param:`day`'s problem using the
    input specified in :param:`input_path`.

    :param input_file: The file to read the input from.
    :param year: The year the problem was released.
    :param day: The day the problem was released.
    :return: The solutions for part 1 and part 2 respectively to the
        specified problem.
    """

    puzzle_input = read_file(input_file=input_file, year=year, day=day)

    module_path = src_path().parts[-1] / year_day_path(year=year, day=day)
    module_path = module_path / module_path.parts[-1]
    module_name = ".".join(module_path.parts)

    solver_name = f"Day{day}"
    solver_module = __import__(module_name, fromlist=[solver_name])
    solver: Solver = getattr(solver_module, solver_name)

    part1_solution = solver.part1(solver.parse(puzzle_input))
    part2_solution = solver.part2(solver.parse(puzzle_input))

    return str(part1_solution), str(part2_solution)
