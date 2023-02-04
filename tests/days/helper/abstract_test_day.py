"""Abstract test class to be used for testing Solution classes."""


from abc import ABC, abstractmethod
from pathlib import Path

import pytest

from advent_of_code_2022.helper.download_files import directory_path, read_file
from advent_of_code_2022.helper.solver import Solver


class AbstractTestDay(ABC):
    """Abstract class to be used for testing solutions."""

    @staticmethod
    @abstractmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """

    @staticmethod
    @abstractmethod
    def solver() -> Solver:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """

    def _parse_input(self, file: Path):
        puzzle_input = read_file(
            input_path=directory_path(self.day()) / file, day=self.day()
        )
        return self.solver().parse(puzzle_input)

    @pytest.fixture(name="example1")
    def fixture_example1(self):
        """Fixture for providing parsed example1 input.

        :return: Parsed example1 input.
        """
        return self._parse_input(Path("example1.txt"))

    @abstractmethod
    def test_parse_example1(self, example1):
        """Test that example input is parsed correctly.

        :param example1: Parsed input from example1 file.
        """

    @abstractmethod
    def test_part1_example1(self, example1):
        """Test part 1 on example input.

        :param example1: Parsed input from example1 file.
        """

    @abstractmethod
    def test_part2_example1(self, example1):
        """Test part 2 on example input.

        :param example1: Parsed input from example1 file.
        """
