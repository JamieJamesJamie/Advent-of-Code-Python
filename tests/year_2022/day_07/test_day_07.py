"""Tests for Day7 Solution class."""


import pytest
from anytree import findall

from advent_of_code.year_2022.day_07.day_07 import Day7, Node
from tests.year_2022.helper.abstract_test_day import AbstractTestDay


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay7(AbstractTestDay):
    """Test class for testing day 7."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 7

    @staticmethod
    def solver() -> type[Day7]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day7

    @staticmethod
    def expected_root() -> Node:
        """Returns the expected parsed tree from the example input.

        :return: The expected parsed tree from the example input.
        """
        return Node(
            "/",
            size=48_381_165,
            children=[
                Node(
                    "a",
                    size=94_853,
                    children=[
                        Node(
                            "e",
                            size=584,
                            children=[
                                Node("i", size=584),
                            ],
                        ),
                        Node("f", size=29_116),
                        Node("g", size=2_557),
                        Node("h.lst", size=62_596),
                    ],
                ),
                Node("b.txt", size=14_848_514),
                Node("c.dat", size=8_504_156),
                Node(
                    "d",
                    size=24_933_642,
                    children=[
                        Node("j", size=4_060_174),
                        Node("d.log", size=8_033_020),
                        Node("d.ext", size=5_626_152),
                        Node("k", size=7_214_296),
                    ],
                ),
            ],
        )

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """

        all_expected_nodes = findall(self.expected_root())
        all_actual_nodes = findall(example)

        assert len(all_expected_nodes) == len(all_actual_nodes)
        assert all(
            all_expected_nodes[i].name == all_actual_nodes[i].name
            and all_expected_nodes[i].size == all_actual_nodes[i].size
            for i in range(len(all_expected_nodes))
        )

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 95_437

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 24_933_642
