"""Solutions for day 3."""


import re

import numpy as np
from scipy.ndimage import correlate, generate_binary_structure, label

from advent_of_code.helper.solver import Solver


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

    _BINRARY_STRUCTURE = generate_binary_structure(2, 2)

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
        # pylint: disable=too-many-locals

        # Get rid of the above pylint disable eventually

        character_map = np.array(tuple(tuple(line) for line in parsed_input))

        numbers = [
            [
                (match.group(0), (match.start(), match.end() - 1))
                for match in re.finditer(r"\d+", line)
            ]
            for line in parsed_input
        ]

        input_np_str = character_map

        is_digits = np.char.isdigit(input_np_str)

        weights = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]

        sums = correlate(is_digits.astype(int), weights)

        gear_bools = (sums >= 2) & (input_np_str == "*")

        thingy10 = np.where(gear_bools, "100", input_np_str)

        input_nums2 = np.where(~np.char.isdigit(thingy10), "0", thingy10)

        input_ints2 = np.asarray(input_nums2, dtype=int)

        correlated3 = correlate(input_ints2, weights)

        correlated_bools3 = correlated3 > (9 * 8)

        numbers_that_touch_symbols_bools3 = correlated_bools3 & is_digits

        s = generate_binary_structure(2, 2)

        labelled_array, num_features = label(
            numbers_that_touch_symbols_bools3 | gear_bools, structure=s
        )

        numbers_that_are_next_to_gears_bool = tuple(
            numbers_that_touch_symbols_bools3 & (labelled_array == feature_num)
            for feature_num in range(1, num_features + 1)
        )

        my_sum = 0

        for gear_map in numbers_that_are_next_to_gears_bool:
            my_mults = []
            my_mult = 1

            for line_index, line in enumerate(numbers):
                for number, (start_index, end_index) in line:
                    if gear_map[line_index, start_index : (end_index + 1)].any():
                        # print(int(number))
                        my_mults.append(int(number))
                        my_mult *= int(number)

            # print(f"gear {gear_index}:", my_mult)

            if len(my_mults) == 2:
                my_sum += np.prod(my_mults)

        # my_sum += int(my_mult)
        # my_sum += np.prod([int(number) for line_index, line in enumerate(numbers)
        # for number, (start_index, end_index) in line
        # if gear_map[line_index, start_index:(end_index + 1)].any()])

        # print("sum:", my_sum)

        return my_sum

        # return sum(
        #     np.prod(
        #         [
        #             int(number)
        #             for line_index, line in enumerate(numbers)
        #             for number, (start_index, end_index) in line
        #             if gear_map[line_index, start_index : (end_index + 1)].any()
        #         ]
        #     )
        #     for gear_index, gear_map in enumerate(numbers_that_are_next_to_gears_bool)
        # )
