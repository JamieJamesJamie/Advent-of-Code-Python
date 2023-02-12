"""Solutions for day 3."""


import textwrap
from collections.abc import Iterable, Sequence

from advent_of_code_2022.helper.solver import Solver


class Day3(Solver):
    """Solver for day 3."""

    @staticmethod
    def _uppercase_priority(character: str) -> int:
        """
        Returns the priority of the given item type :param:`character` given that
        :param:`character` is uppercase.

        :param character: The item type to get the priority of.
        :return: The priority of the given item type.
        """
        return ord(character) - ord("A") + 27

    @staticmethod
    def _lowercase_priority(character: str) -> int:
        """
        Returns the priority of the given item type :param:`character` given that
        :param:`character` is lowercase.

        :param character: The item type to get the priority of.
        :return: The priority of the given item type.
        """
        return ord(character) - ord("a") + 1

    @staticmethod
    def _character_priority(character: str) -> int:
        """Returns the priority of the given item type :param:`character`.

        :param character: The item type to get the priority of.
        :return: The priority of the given item type.
        """
        return (
            Day3._uppercase_priority(character)
            if character.isupper()
            else Day3._lowercase_priority(character)
        )

    @staticmethod
    def parse(puzzle_input: str) -> tuple[str, ...]:
        """Parse input for puzzle 3.

        :param puzzle_input: Input to parse.
        :return: The contents contained in each rucksack.
        """
        return tuple(puzzle_input.split("\n"))

    @staticmethod
    def part1(parsed_input: Iterable[str]) -> int:
        """Solves part 1.

        :param parsed_input: The contents contained in each rucksack.
        :return: The sum of the priorities of each item that appears in both
            compartments in each rucksack.
        """
        summed_priorities = 0

        for rucksack in parsed_input:
            compartments = textwrap.wrap(rucksack, len(rucksack) // 2)
            shared_character = (
                set(compartments[0]).intersection(set(compartments[1])).pop()
            )
            summed_priorities += Day3._character_priority(shared_character)

        return summed_priorities

    @staticmethod
    def part2(parsed_input: Sequence[str]) -> int:
        """Solves part 2.

        :param parsed_input: The contents contained in each rucksack.
        :return: The sum of the priorities of each group's badge.
        """
        summed_priorities = 0

        for grouped_rucksacks in zip(
            parsed_input[::3], parsed_input[1::3], parsed_input[2::3]
        ):
            shared_character = set.intersection(
                *(set(rucksack) for rucksack in grouped_rucksacks)
            ).pop()
            summed_priorities += Day3._character_priority(shared_character)

        return summed_priorities
