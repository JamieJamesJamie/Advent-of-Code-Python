"""Tests for Day12 Solution class."""


import pytest

from advent_of_code.year_2022.day_12.day_12 import Day12
from tests.year_2022.abstract_test_day_2022 import AbstractTestDay2022


@pytest.mark.parametrize("example", [1], indirect=True)
class TestDay(AbstractTestDay2022):
    """Test class for testing day 12."""

    @staticmethod
    def day() -> int:
        """Returns the day that is being tested.

        :return: The day that is being tested.
        """
        return 12

    @staticmethod
    def solver() -> type[Day12]:
        """Returns the Solver class that is being tested.

        :return: The solver class that is being tested.
        """
        return Day12

    def test_parse_example(self, example):
        """Test that example input is parsed correctly.

        :param example: Parsed input from example file.
        """
        assert example.adj == {
            ("S", 0, 0): {("a", 1, 0): {}, ("a", 0, 1): {}},
            ("a", 0, 1): {("S", 0, 0): {}, ("b", 1, 1): {}, ("b", 0, 2): {}},
            ("b", 0, 2): {("a", 0, 1): {}, ("c", 1, 2): {}},
            ("q", 0, 3): {("b", 0, 2): {}, ("r", 1, 3): {}, ("p", 0, 4): {}},
            ("p", 0, 4): {("q", 0, 3): {}, ("o", 0, 5): {}},
            ("o", 0, 5): {("p", 0, 4): {}, ("n", 0, 6): {}},
            ("n", 0, 6): {("o", 0, 5): {}, ("m", 0, 7): {}},
            ("m", 0, 7): {("n", 0, 6): {}, ("l", 1, 7): {}},
            ("a", 1, 0): {("S", 0, 0): {}, ("a", 2, 0): {}, ("b", 1, 1): {}},
            ("b", 1, 1): {
                ("a", 1, 0): {},
                ("a", 0, 1): {},
                ("c", 2, 1): {},
                ("c", 1, 2): {},
            },
            ("c", 1, 2): {("b", 1, 1): {}, ("b", 0, 2): {}, ("c", 2, 2): {}},
            ("r", 1, 3): {("c", 1, 2): {}, ("q", 0, 3): {}, ("s", 2, 3): {}},
            ("y", 1, 4): {
                ("r", 1, 3): {},
                ("p", 0, 4): {},
                ("z", 2, 4): {},
                ("x", 1, 5): {},
            },
            ("x", 1, 5): {("y", 1, 4): {}, ("o", 0, 5): {}, ("x", 1, 6): {}},
            ("x", 1, 6): {
                ("x", 1, 5): {},
                ("n", 0, 6): {},
                ("x", 2, 6): {},
                ("l", 1, 7): {},
            },
            ("l", 1, 7): {("m", 0, 7): {}, ("k", 2, 7): {}},
            ("a", 2, 0): {("a", 1, 0): {}, ("a", 3, 0): {}},
            ("c", 2, 1): {
                ("a", 2, 0): {},
                ("b", 1, 1): {},
                ("c", 3, 1): {},
                ("c", 2, 2): {},
            },
            ("c", 2, 2): {("c", 2, 1): {}, ("c", 1, 2): {}, ("c", 3, 2): {}},
            ("s", 2, 3): {("c", 2, 2): {}, ("r", 1, 3): {}, ("t", 3, 3): {}},
            ("z", 2, 4): {
                ("s", 2, 3): {},
                ("y", 1, 4): {},
                ("u", 3, 4): {},
                ("E", 2, 5): {},
            },
            ("E", 2, 5): {
                ("z", 2, 4): {},
                ("x", 1, 5): {},
                ("v", 3, 5): {},
                ("x", 2, 6): {},
            },
            ("x", 2, 6): {("x", 1, 6): {}, ("w", 3, 6): {}, ("k", 2, 7): {}},
            ("k", 2, 7): {("l", 1, 7): {}, ("j", 3, 7): {}},
            ("a", 3, 0): {("a", 2, 0): {}, ("a", 4, 0): {}},
            ("c", 3, 1): {
                ("a", 3, 0): {},
                ("c", 2, 1): {},
                ("b", 4, 1): {},
                ("c", 3, 2): {},
            },
            ("c", 3, 2): {("c", 3, 1): {}, ("c", 2, 2): {}, ("d", 4, 2): {}},
            ("t", 3, 3): {
                ("c", 3, 2): {},
                ("s", 2, 3): {},
                ("e", 4, 3): {},
                ("u", 3, 4): {},
            },
            ("u", 3, 4): {("t", 3, 3): {}, ("f", 4, 4): {}, ("v", 3, 5): {}},
            ("v", 3, 5): {("u", 3, 4): {}, ("g", 4, 5): {}, ("w", 3, 6): {}},
            ("w", 3, 6): {
                ("v", 3, 5): {},
                ("x", 2, 6): {},
                ("h", 4, 6): {},
                ("j", 3, 7): {},
            },
            ("j", 3, 7): {("k", 2, 7): {}, ("i", 4, 7): {}},
            ("a", 4, 0): {("a", 3, 0): {}, ("b", 4, 1): {}},
            ("b", 4, 1): {("a", 4, 0): {}, ("c", 3, 1): {}},
            ("d", 4, 2): {("b", 4, 1): {}, ("c", 3, 2): {}, ("e", 4, 3): {}},
            ("e", 4, 3): {("d", 4, 2): {}, ("f", 4, 4): {}},
            ("f", 4, 4): {("e", 4, 3): {}, ("g", 4, 5): {}},
            ("g", 4, 5): {("f", 4, 4): {}, ("h", 4, 6): {}},
            ("h", 4, 6): {("g", 4, 5): {}, ("i", 4, 7): {}},
            ("i", 4, 7): {("h", 4, 6): {}, ("j", 3, 7): {}},
        }

    def test_part1_example(self, example):
        """Test part 1 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part1(example) == 31

    def test_part2_example(self, example):
        """Test part 2 on example input.

        :param example: Parsed input from example file.
        """
        assert self.solver().part2(example) == 29
