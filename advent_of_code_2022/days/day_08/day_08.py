"""Solutions for day 8."""

import numpy as np

from advent_of_code_2022.helper.solver import Solver


class Day8(Solver):
    """Solver for day 8."""

    @staticmethod
    def parse(puzzle_input: str) -> np.ndarray:
        """Parse input for puzzle 8.

        :param puzzle_input: Input to parse.
        :return: The forest map.
        """
        return np.array(
            [
                [int(character) for character in line.rstrip()]
                for line in puzzle_input.split("\n")
            ],
            dtype=np.int8,
        )

    @staticmethod
    def part1(parsed_input: np.ndarray) -> int:
        """Solves part 1.

        :param parsed_input: The forest map.
        :return: The number of trees visible from outside the grid.
        """
        mask = np.asarray(
            [
                [
                    any(
                        (parsed_input[row_i, col_i] > other_trees).all()
                        for other_trees in (
                            parsed_input[row_i, :col_i],  # left trees
                            parsed_input[row_i, (col_i + 1) :],  # right trees
                            parsed_input[:row_i, col_i],  # top trees
                            parsed_input[(row_i + 1) :, col_i],  # bottom trees
                        )
                    )
                    for col_i, col in enumerate(row)
                ]
                for row_i, row in enumerate(parsed_input)
            ]
        )

        return parsed_input[mask].size

    @staticmethod
    def part2(parsed_input: np.ndarray) -> int:
        """Solves part 2.

        :param parsed_input: The forest map.
        :return: The maximum scenic score possible for any tree.
        """
        scenic_score = np.zeros(parsed_input.shape, dtype=int)

        for row_i, row in enumerate(parsed_input):
            for col_i in range(len(row)):
                other_trees_all_directions = [
                    # left trees in order from (x, y)
                    parsed_input[row_i, (col_i - 1) :: -1]
                    if col_i != 0
                    else np.array([]),
                    # right trees in order from (x, y)
                    parsed_input[row_i, (col_i + 1) :]
                    if col_i != parsed_input.shape[1] - 1
                    else np.array([]),
                    # top trees in order from (x, y)
                    parsed_input[(row_i - 1) :: -1, col_i]
                    if row_i != 0
                    else np.array([]),
                    # bottom trees in order from (x, y)
                    parsed_input[(row_i + 1) :, col_i]
                    if row_i != parsed_input.shape[0] - 1
                    else np.array([]),
                ]

                num_trees_that_can_be_seen = np.zeros(len(other_trees_all_directions))

                for direction, other_trees_specific_direction in enumerate(
                    other_trees_all_directions
                ):
                    for tree in other_trees_specific_direction:
                        num_trees_that_can_be_seen[direction] += 1

                        if tree >= parsed_input[row_i, col_i]:
                            break

                scenic_score[row_i, col_i] = np.prod(num_trees_that_can_be_seen)

        return np.max(scenic_score)
