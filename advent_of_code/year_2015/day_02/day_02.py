"""Solutions for day 2."""

import itertools
import math

from advent_of_code.helper.solver import Solver


class Day2(Solver):
    """Solver for day 2."""

    @staticmethod
    def parse(puzzle_input: str) -> tuple[tuple[int, ...], ...]:
        """Parse input for puzzle 2.

        :param puzzle_input: Input to parse.
        :return: The dimensions of each present.
        """
        return tuple(
            tuple(int(number) for number in line.split("x"))
            for line in puzzle_input.splitlines()
        )

    @staticmethod
    def part1(parsed_input: tuple[tuple[int, ...], ...]) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The required total area of wrapping paper.
        """
        face_area_components = tuple(
            tuple(
                math.prod(combination)
                for combination in itertools.combinations(dimension, 2)
            )
            for dimension in parsed_input
        )

        min_areas = (min(areas) for areas in face_area_components)

        all_areas = (sum(2 * area for area in areas) for areas in face_area_components)

        return sum(itertools.chain(*zip(all_areas, min_areas)))

    @staticmethod
    def part2(parsed_input: tuple[tuple[int, ...], ...]) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The required total length of ribbon.
        """
        smallest_present_perimeters = (
            min(
                2 * sum(combination)
                for combination in itertools.combinations(dimension, 2)
            )
            for dimension in parsed_input
        )

        bow_lengths = (math.prod(measurements) for measurements in parsed_input)

        return sum(itertools.chain(*zip(smallest_present_perimeters, bow_lengths)))
