"""Solutions for day 4."""


from collections.abc import Iterable

from advent_of_code.helper.solver import Solver


class Day4(Solver):
    """Solver for day 4."""

    @staticmethod
    def parse(puzzle_input: str) -> tuple[int, ...]:
        return tuple(
            len(
                set.intersection(
                    *(
                        {int(number) for number in numbers.split()}
                        for numbers in line.split(":")[1].split("|")
                    )
                )
            )
            for line in puzzle_input.splitlines()
        )

    @staticmethod
    def part1(parsed_input: Iterable[int]) -> int:
        return sum(int(2 ** (matches - 1)) for matches in parsed_input)

    @staticmethod
    def part2(parsed_input: Iterable[int]) -> int:
        pass
