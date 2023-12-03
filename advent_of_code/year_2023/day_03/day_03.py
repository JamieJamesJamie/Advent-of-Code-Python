"""Solutions for day 3."""


import re

import numpy as np
from scipy.ndimage import correlate

from advent_of_code.helper.solver import Solver


class Day3(Solver):
    """Solver for day 3."""

    @staticmethod
    def parse(puzzle_input: str) -> tuple[str, ...]:
        return tuple(puzzle_input.split("\n"))

    @staticmethod
    def part1(parsed_input: tuple[str, ...]) -> int:
        """Solves part 1.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """
        character_map = np.array(tuple(tuple(line) for line in parsed_input))

        replaced_dots = np.where(character_map == ".", "0", character_map)
        digit_map = np.where(~np.char.isdigit(replaced_dots), "100", replaced_dots)
        int_map = np.asarray(digit_map, dtype=int)

        weights = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]

        correlated = correlate(int_map, weights)

        max_digit = 9
        num_weights = sum(sum(weight) for weight in weights)

        does_touch_symbol = correlated > (max_digit * num_weights)

        number_does_touch_symbol = does_touch_symbol & np.char.isdigit(character_map)

        numbers = [
            [
                (match.group(0), (match.start(), match.end() - 1))
                for match in re.finditer(r"\d+", line)
            ]
            for line in parsed_input
        ]

        return sum(
            int(number)
            for line_index, line in enumerate(numbers)
            for number, (start_index, end_index) in line
            if number_does_touch_symbol[line_index, start_index : (end_index + 1)].any()
        )

    @staticmethod
    def part2(parsed_input: tuple[str, ...]) -> int:
        """Solves part 2.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """
        return 0
