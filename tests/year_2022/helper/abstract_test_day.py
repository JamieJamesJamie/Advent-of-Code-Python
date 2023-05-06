"""Abstract test class to be used for testing Solution classes."""


from abc import ABC, abstractmethod

import pytest

from advent_of_code.helper.download_files import directory_path, read_file
from advent_of_code.helper.solver import Solver


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
    def solver() -> type[Solver]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """

    def _parse_input(self, example_number: int):
        puzzle_input = read_file(
            input_path=directory_path(self.day()) / f"example{example_number}.txt",
            day=self.day(),
        )
        return self.solver().parse(puzzle_input)

    @pytest.fixture(name="example")
    def fixture_example(self, request):
        """Fixture for providing parsed example input.

        :return: Parsed example input.
        """
        return self._parse_input(request.param)

    @abstractmethod
    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """

    @abstractmethod
    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """

    @abstractmethod
    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
