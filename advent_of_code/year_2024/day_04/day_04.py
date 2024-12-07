"""Solutions for day 4."""

from functools import partial
from itertools import product

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from scipy.ndimage import correlate

from advent_of_code.helper.solver import Solver


class Day4(Solver):
    """Solver for day 4."""

    _XMAS_ARRAY = np.array(tuple("XMAS"))

    _X_MAS_MAPPING = {"X": 0, "M": 1, "A": 2, "S": 4}

    _WEIGHTS = (
        (
            (1, 0, 0),
            (0, 0, 0),
            (0, 0, 1),
        ),
        (
            (0, 0, 1),
            (0, 0, 0),
            (1, 0, 0),
        ),
    )

    _X_MIDDLE_MS = _X_MAS_MAPPING["M"] + _X_MAS_MAPPING["S"]

    _CORRELATION_MODE = "constant"

    @staticmethod
    def _flip_functions(axis: int):
        return np.asarray, partial(np.flip, axis=axis)

    @staticmethod
    def _num_occurrences(horizontal_array: np.ndarray) -> int:
        return np.sum(np.all(horizontal_array == Day4._XMAS_ARRAY, 1))

    @staticmethod
    def _non_diagonal_sum(
        word_search: np.ndarray, window_shape: tuple[int, int]
    ) -> int:
        windows = sliding_window_view(word_search, window_shape)
        reshaped_windows = windows.reshape((np.multiply(*windows.shape[0:2]), 4))

        return sum(
            Day4._num_occurrences(flip_function(reshaped_windows))
            for flip_function in Day4._flip_functions(1)
        )

    @staticmethod
    def _horizontal_sum(word_search: np.ndarray) -> int:
        return Day4._non_diagonal_sum(word_search, (1, 4))

    @staticmethod
    def _vertical_sum(word_search: np.ndarray) -> int:
        return Day4._non_diagonal_sum(word_search, (4, 1))

    @staticmethod
    def _diagonal_sum(word_search: np.ndarray) -> int:
        windows = sliding_window_view(word_search, (4, 4))
        reshaped_windows = windows.reshape((np.multiply(*windows.shape[0:2]), 4, 4))

        return sum(
            Day4._num_occurrences(
                flip_function_1(flip_function_2(reshaped_windows)).diagonal(
                    axis1=1, axis2=2
                )
            )
            for flip_function_1, flip_function_2 in product(
                Day4._flip_functions(1), Day4._flip_functions(2)
            )
        )

    @staticmethod
    def parse(puzzle_input: str) -> np.ndarray:
        """Parse input for puzzle 4.

        :param puzzle_input: Input to parse.
        :return: The characters in the word search.
        """
        return np.array(tuple(tuple(line) for line in puzzle_input.splitlines()))

    @staticmethod
    def part1(parsed_input: np.ndarray) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The number of times "XMAS" appears in the word search.
        """
        return sum(
            (
                Day4._horizontal_sum(parsed_input),
                Day4._vertical_sum(parsed_input),
                Day4._diagonal_sum(parsed_input),
            )
        )

    @staticmethod
    def part2(parsed_input: np.ndarray) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The number of "X-MAS" occurrences in the word search.
        """
        letter_number_mapping = np.array(
            tuple(
                tuple(Day4._X_MAS_MAPPING[character] for character in line)
                for line in parsed_input
            )
        )

        a_locations = letter_number_mapping == Day4._X_MAS_MAPPING["A"]

        correlated = (
            correlate(
                letter_number_mapping, Day4._WEIGHTS[0], mode=Day4._CORRELATION_MODE
            ),
            correlate(
                letter_number_mapping, Day4._WEIGHTS[1], mode=Day4._CORRELATION_MODE
            ),
        )

        cross_middles = (correlated[0] == Day4._X_MIDDLE_MS) & (
            correlated[1] == Day4._X_MIDDLE_MS
        )

        mas_locations = a_locations & cross_middles

        return np.sum(mas_locations)
