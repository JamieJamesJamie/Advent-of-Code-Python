"""Solutions for day 4."""

import itertools
from hashlib import md5

from advent_of_code.helper.solver import Solver


class Day4(Solver):
    """Solver for day 4."""

    @staticmethod
    def _find_md5_hash(key_prefix: str, num_leading_zeros: int) -> int:
        """Finds the smallest key suffix that produces an MD5 hash with the
        specified number of leading zeros.

        :param key_prefix: The prefix of the MD5 key.
        :param num_leading_zeros: The number of leading zeros that the
            MD5 hash should have.
        :return: The smallest key suffix that produces an MD5 hash with
            the specified number of leading zeros.
        """
        for number in itertools.count(1):
            if (
                md5(f"{key_prefix}{number}".encode(), usedforsecurity=False)
                .hexdigest()
                .startswith("0" * num_leading_zeros)
            ):
                return number

        raise NotImplementedError(
            "Function should never raise this error, "
            "but this error is needed to satisfy mypy"
        )

    @staticmethod
    def parse(puzzle_input: str) -> str:
        """Parse input for puzzle 4.

        :param puzzle_input: The input to parse.
        :return: The key prefix.
        """
        return puzzle_input

    @staticmethod
    def part1(parsed_input: str) -> int:
        """Solves part 1.

        :param parsed_input: Input to parse.
        :return: The smallest key suffix that produces an MD5 hash with
            5 leading zeros.
        """
        return Day4._find_md5_hash(parsed_input, 5)

    @staticmethod
    def part2(parsed_input: str) -> int:
        """Solves part 2.

        :param parsed_input: Input to parse.
        :return: The smallest key suffix that produces an MD5 hash with
            6 leading zeros.
        """
        return Day4._find_md5_hash(parsed_input, 6)
