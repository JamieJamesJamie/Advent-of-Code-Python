"""Solutions for day 12."""

from collections import defaultdict

import networkx as nx
import numpy as np

from advent_of_code.helper.solver import Solver


class Day12(Solver):
    """Solver for day 12."""

    @staticmethod
    def character_to_height(character: str) -> int:
        """Returns the numerical height represented by the :param:`character`.

        :param character: The character representation of an elevation.
        :return: The numerical representation of an elevation.
        """
        if character == "S":
            character = "a"
        elif character == "E":
            character = "z"

        return ord(character) - (ord("a") - 1)

    @staticmethod
    def parse(puzzle_input: str) -> nx.DiGraph:
        """Parse input for puzzle 12.

        :param puzzle_input: Input to parse.
        :return: A digraph representing the possible paths.
        """
        heightmap_character_array = np.array(
            [list(line.rstrip()) for line in puzzle_input.splitlines()]
        )

        heightmap_int_array = np.vectorize(Day12.character_to_height)(
            heightmap_character_array
        )

        neighbours_dict_of_lists = defaultdict(list)

        for pixel in range(np.prod(heightmap_int_array.shape)):
            grid_height, grid_width = heightmap_int_array.shape

            pixel_row = pixel // grid_width
            pixel_column = pixel % grid_width

            for x_increment in range(3):
                neighbour_column = pixel_column + x_increment - 1

                for y_increment in range(3):
                    neighbour_row = pixel_row + y_increment - 1

                    if (
                        0 <= neighbour_row < grid_height
                        and 0 <= neighbour_column < grid_width
                        and abs(y_increment - x_increment) == 1
                        and heightmap_int_array[pixel_row, pixel_column]
                        - heightmap_int_array[neighbour_row, neighbour_column]
                        >= -1
                    ):
                        neighbours_dict_of_lists[
                            (
                                heightmap_character_array[pixel_row, pixel_column],
                                pixel_row,
                                pixel_column,
                            )
                        ].append(
                            (
                                heightmap_character_array[
                                    neighbour_row, neighbour_column
                                ],
                                neighbour_row,
                                neighbour_column,
                            )
                        )

        # neighbours_dict_of_lists = {
        #     (
        #         heightmap_character_array[
        #             p // heightmap_int_array.shape[1],
        #             p % heightmap_int_array.shape[1],
        #         ],
        #         p // heightmap_int_array.shape[1],
        #         p % heightmap_int_array.shape[1],
        #     ): [
        #         (
        #             heightmap_character_array[
        #                 p // heightmap_int_array.shape[1] + y_inc - 1,
        #                 p % heightmap_int_array.shape[1] + x_inc - 1,
        #             ],
        #             p // heightmap_int_array.shape[1] + y_inc - 1,
        #             p % heightmap_int_array.shape[1] + x_inc - 1,
        #         )
        #         for y_inc in range(3)
        #         if 1
        #         <= p // heightmap_int_array.shape[1] + y_inc
        #         <= heightmap_int_array.shape[0]
        #         for x_inc in range(3)
        #         if heightmap_int_array.shape[1]
        #         >= p % heightmap_int_array.shape[1] + x_inc
        #         >= 1
        #         == abs(y_inc - x_inc)
        #         and heightmap_int_array[
        #             p // heightmap_int_array.shape[1],
        #             p % heightmap_int_array.shape[1],
        #         ]
        #         - heightmap_int_array[
        #             p // heightmap_int_array.shape[1] + y_inc - 1,
        #             p % heightmap_int_array.shape[1] + x_inc - 1,
        #         ]
        #         >= -1
        #     ]
        #     for p in range(np.prod(heightmap_int_array.shape))
        # }

        return nx.DiGraph(neighbours_dict_of_lists)

    @staticmethod
    def part1(parsed_input: nx.DiGraph) -> int:
        """Solves part 1.

        :param parsed_input: A digraph representing the possible paths.
        :return: The length of the shortest path between "S" and "E".
        """
        # nx.draw_networkx(
        #     parsed_input,
        #     arrows=True,
        #     pos=nx.spring_layout(parsed_input),
        # )
        # plt.show()

        return nx.shortest_path_length(
            parsed_input,
            source=next(node for node in parsed_input.nodes if node[0] == "S"),
            target=next(node for node in parsed_input.nodes if node[0] == "E"),
        )

    @staticmethod
    def part2(parsed_input: nx.DiGraph) -> int:
        """Solves part 2.

        :param parsed_input: A digraph representing the possible paths.
        :return: The length of the shortest path between any "a" (or
            "S") and "E".
        """
        target = next(node for node in parsed_input.nodes if node[0] == "E")

        steps = []
        for node in parsed_input.nodes:
            if node[0] == "S" or node[0] == "a":
                try:
                    steps.append(
                        nx.shortest_path_length(
                            parsed_input, source=node, target=target
                        )
                    )
                except nx.NetworkXNoPath:
                    pass

        return min(steps)
