"""Solutions for day 4."""


from itertools import permutations

from advent_of_code_2022.helper.helper import inclusive_range
from advent_of_code_2022.helper.solver import Solver


class Day4(Solver):
    """Solver for day 4."""

    @staticmethod
    def parse(puzzle_input: str) -> tuple[tuple[set[int], ...], ...]:
        """Parse input for puzzle 4.

        :param puzzle_input: Input to parse.
        :return: The section IDs that each elf pair has been assigned.
        """
        return tuple(
            tuple(
                set(
                    inclusive_range(
                        *tuple(int(boundary) for boundary in elf_boundaries.split("-"))
                    )
                )
                for elf_boundaries in section_assignment_pair.split(",")
            )
            for section_assignment_pair in puzzle_input.split("\n")
        )

    @staticmethod
    def part1(parsed_input: tuple[tuple[set[int], ...], ...]) -> int:
        """Solves part 1.

        :param parsed_input: The section IDs that each elf pair has been assigned.
        :return: The number of assignment pairs where one assignment fully contains
            the other assignment.
        """
        return sum(
            any(
                set1.issubset(set2)
                for set1, set2 in permutations(section_assignment_pair)
            )
            for section_assignment_pair in parsed_input
        )

    @staticmethod
    def part2(parsed_input: tuple[tuple[set[int], ...], ...]) -> int:
        """Solves part 2.

        :param parsed_input: The section IDs that each elf pair has been assigned.
        :return: The number of assignment pairs where one assignment overlaps the other
            assignment.
        """
        return sum(bool(set1.intersection(set2)) for set1, set2 in parsed_input)
