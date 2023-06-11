"""Solutions for day 14."""

from collections.abc import Iterable
from enum import Enum
from itertools import product
from typing import NamedTuple

from advent_of_code.helper.solver import Solver


class Element(Enum):
    """Element within the cave."""

    ROCK = "#"
    SAND = "o"


class Position(NamedTuple):
    """The position of an element within the cave."""

    x: int
    y: int


class Day14(Solver):
    """Solver for day 14."""

    @staticmethod
    def _parse_path(path: str) -> tuple[Position, ...]:
        """Parses the path represented by a line of the puzzle input.

        :param path: A path represented by the puzzle input.
        :return: The coordinates along the given path.
        """
        coordinates = path.split(" -> ")
        return tuple(
            Position(*rock_coordinate)
            for coordinate1, coordinate2 in zip(coordinates, coordinates[1:])
            for rock_coordinate in Day14._parse_straight_line(
                coordinate1.split(","), coordinate2.split(",")
            )
        )

    @staticmethod
    def _parse_straight_line(
        coordinate1_string: Iterable[str], coordinate2_string: Iterable[str]
    ) -> Iterable[tuple[int, int]]:
        """Parses the given coordinates representing the ends of a straight
        line, and returns each coordinate on this straight line.

        :param coordinate1_string: An iterable containing 2 coordinates
            as strings.
        :param coordinate2_string: An iterable containing 2 coordinates
            as strings.
        :return: Each coordinate along the straight line represented by
            the given coordinates.
        """
        coordinate1 = Position(*(int(dim) for dim in coordinate1_string))
        coordinate2 = Position(*(int(dim) for dim in coordinate2_string))

        return product(
            range(coordinate1.x, coordinate2.x + 1)
            if coordinate1.x <= coordinate2.x
            else range(coordinate2.x, coordinate1.x + 1),
            range(coordinate1.y, coordinate2.y + 1)
            if coordinate1.y <= coordinate2.y
            else range(coordinate2.y, coordinate1.y + 1),
        )

    @staticmethod
    def parse(puzzle_input: str) -> dict[Position, Element]:
        """Parse input for puzzle 14.

        :param puzzle_input: Input to parse.
        :return: Mapping from positions to ROCK elements.
        """
        return {
            rock_coordinate: Element.ROCK
            for line in puzzle_input.split("\n")
            for rock_coordinate in Day14._parse_path(line)
        }

    @staticmethod
    def _simulate_sand_unit(
        cave_map: dict[Position, Element],
        void_y_coordinate: int,
        sand_source: Position = Position(500, 0),
    ) -> Position | None:
        """Simulates a single unit of sand falling from the
        :param:`sand_source`.

        :param cave_map: Mapping from positions to elements.
        :param void_y_coordinate: The point at which sand will fall into the void.
        :param sand_source: The source of sand.
        :return: Position the sand settles, or :code:`None` if the unit of sand falls
            into the void.
        """
        x_coordinate = sand_source[0]

        for y_coordinate in range(sand_source[1], void_y_coordinate + 1):
            if Position(x_coordinate, y_coordinate + 1) not in cave_map:
                continue

            if Position(x_coordinate - 1, y_coordinate + 1) not in cave_map:
                x_coordinate -= 1
                continue

            if Position(x_coordinate + 1, y_coordinate + 1) not in cave_map:
                x_coordinate += 1
                continue

            return Position(x_coordinate, y_coordinate)

        return None

    @staticmethod
    def _simulate_sand(
        cave_map: dict[Position, Element],
        void_y_coordinate: int,
        sand_source: Position = Position(500, 0),
    ) -> dict[Position, Element]:
        """Simulates sand falling from the :param:`sand_source`.

        :param cave_map: Mapping from positions to elements.
        :param void_y_coordinate: The point at which sand will fall into the void.
        :param sand_source: The source of sand.
        :return: Mapping from positions to elements.
        """
        while True:
            sand_position = Day14._simulate_sand_unit(
                cave_map, void_y_coordinate, sand_source
            )

            if sand_position is None:
                return cave_map

            cave_map |= {sand_position: Element.SAND}

            if sand_position == sand_source:
                return cave_map

    @staticmethod
    def part1(parsed_input: dict[Position, Element]) -> int:
        """Solves part 1.

        :param parsed_input: Mapping from positions to ROCK elements.
        :return: The number of units of sand that have come to rest
            before sand starts flowing into the void below.
        """
        void_y_coordinate = max(y_coordinate for _, y_coordinate in parsed_input.keys())
        cave_map = Day14._simulate_sand(parsed_input, void_y_coordinate)
        return sum(element == Element.SAND for element in cave_map.values())

    @staticmethod
    def part2(parsed_input: dict[Position, Element]) -> int:
        """Solves part 2.

        :param parsed_input: Mapping from positions to ROCK elements.
        :return: The number of units of sand that have come to rest.
        """
        floor_y_coordinate = (
            max(y_coordinate for _, y_coordinate in parsed_input.keys()) + 2
        )
        num_floor_elements = 2 * floor_y_coordinate + 1
        sand_source = Position(500, 0)

        cave_map = Day14._simulate_sand(
            parsed_input
            | {
                Position(floor_x_coordinate, floor_y_coordinate): Element.ROCK
                for floor_x_coordinate in range(
                    sand_source.x - (num_floor_elements // 2),
                    sand_source.x + (num_floor_elements // 2) + 1,
                )
            },
            floor_y_coordinate,
            sand_source,
        )

        return sum(element == Element.SAND for element in cave_map.values())
