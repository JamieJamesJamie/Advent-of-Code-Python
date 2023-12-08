"""Solutions for day 3."""


import re
from collections.abc import Iterable

import numpy as np
from scipy.ndimage import correlate, generate_binary_structure, label

from advent_of_code.helper.solver import Solver


class ParsedInput:
    """Represents the parsed input."""

    # pylint: disable=too-few-public-methods

    def __init__(self, puzzle_input: str):
        lines = puzzle_input.splitlines()

        self.character_map = np.array(tuple(tuple(line) for line in lines))
        self.character_map.flags.writeable = False

        self.numbers = tuple(
            tuple(
                (int(match.group(0)), (match.start(), match.end() - 1))
                for match in re.finditer(r"\d+", line)
            )
            for line in lines
        )


class Day3(Solver):
    """Solver for day 3."""

    _WEIGHTS = (
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1),
    )

    _NUM_WEIGHTS = sum(sum(weight) for weight in _WEIGHTS)

    _MAXIMUM_DIGIT = 9

    _KERNEL_BOUNDARY = _NUM_WEIGHTS * _MAXIMUM_DIGIT

    _BINARY_STRUCTURE = generate_binary_structure(2, 2)

    @staticmethod
    def _calculate_calibration_sum_part_2(
        numbers_that_are_next_to_gears_bool: Iterable[np.ndarray],
        numbers: Iterable[Iterable[tuple[int, tuple[int, int]]]],
    ) -> int:
        result = 0

        for gear_map in numbers_that_are_next_to_gears_bool:
            operands = []
            mult = 1

            for line_index, line in enumerate(numbers):
                for number, (start_index, end_index) in line:
                    if gear_map[line_index, start_index : (end_index + 1)].any():
                        operands.append(number)
                        mult *= number

            if len(operands) == 2:
                result += int(np.prod(operands))

        return result

    @staticmethod
    def parse(puzzle_input: str) -> ParsedInput:
        return ParsedInput(puzzle_input)

    @staticmethod
    def part1(parsed_input: ParsedInput) -> int:
        """Solves part 1.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """

        replaced_dots = np.where(
            parsed_input.character_map == ".", "0", parsed_input.character_map
        )
        digit_map = np.where(~np.char.isdigit(replaced_dots), "100", replaced_dots)
        int_map = digit_map.astype(int)

        correlated = correlate(int_map, Day3._WEIGHTS)

        does_touch_symbol = correlated > Day3._KERNEL_BOUNDARY

        number_does_touch_symbol = does_touch_symbol & np.char.isdigit(
            parsed_input.character_map
        )

        return sum(
            int(number)
            for line_index, line in enumerate(parsed_input.numbers)
            for number, (start_index, end_index) in line
            if number_does_touch_symbol[line_index, start_index : (end_index + 1)].any()
        )

    @staticmethod
    def part2(parsed_input: ParsedInput) -> int:
        """Solves part 2.

        :param parsed_input: The lines to use for calibration.
        :return: The summed calibration values.
        """
        is_digits = np.char.isdigit(parsed_input.character_map)
        sums = correlate(is_digits.astype(int), Day3._WEIGHTS)
        gear_bools = (sums >= 2) & (parsed_input.character_map == "*")

        gear_nums = np.where(gear_bools, "100", parsed_input.character_map)
        input_nums = np.where(~np.char.isdigit(gear_nums), "0", gear_nums)
        input_ints = input_nums.astype(int)

        correlated = correlate(input_ints, Day3._WEIGHTS)
        correlated_bools = correlated > Day3._KERNEL_BOUNDARY
        numbers_that_touch_symbols_bools = correlated_bools & is_digits

        labelled_array, num_features = label(
            numbers_that_touch_symbols_bools | gear_bools,
            structure=Day3._BINARY_STRUCTURE,
        )

        numbers_that_are_next_to_gears_bool = tuple(
            numbers_that_touch_symbols_bools & (labelled_array == feature_num)
            for feature_num in range(1, num_features + 1)
        )

        return Day3._calculate_calibration_sum_part_2(
            numbers_that_are_next_to_gears_bool, parsed_input.numbers
        )
