"""Solutions for day 1."""

from collections.abc import Iterable

from advent_of_code.helper.solver import Solver


class Day1(Solver):
    """Solver for day 1."""

    @staticmethod
    def parse(puzzle_input: str) -> tuple[int, ...]:
        """Parse input for puzzle 1.

        :param puzzle_input: Input to parse.
        :return: The total calories each elf is carrying.
        """
        return tuple(
            sum(
                int(elf_individual_calories)
                for elf_individual_calories in elf_all_calories.splitlines()
            )
            for elf_all_calories in puzzle_input.split("\n\n")
        )

    @staticmethod
    def part1(parsed_input: Iterable[int]) -> int:
        """Solves part 1.

        :param parsed_input: The calories being carried by each elf in
            order.
        :return: The maximum number of calories being carried by an elf.
        """
        return max(parsed_input)

    @staticmethod
    def part2(parsed_input: Iterable[int]) -> int:
        """Solves part 2.

        :param parsed_input: The calories being carried by each elf in
            order.
        :return: The sum of the top 3 elves carrying the most calories.
        """
        return sum(sorted(parsed_input)[-3:])
