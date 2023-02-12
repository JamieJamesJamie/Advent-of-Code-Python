"""Solutions for day 6."""

from collections import deque

from advent_of_code_2022.helper.solver import Solver


class Day6(Solver):
    """Solver for day 6."""

    @staticmethod
    def _get_marker(datastream_buffer: str, num_distinct_characters: int) -> int:
        """Returns the marker for the specified :param:`datastream_buffer`
        given the number of distinct characters
        :param:`num_distinct_characters` that there should be to indicate a
        marker.

        :param datastream_buffer: The datastream buffer received by the device.
        :param num_distinct_characters: The number of distinct characters that there
            should be to indicate a marker.
        :return: The number of characters that need to be processed before the marker is
            detected.
        """
        window: deque[str] = deque(maxlen=num_distinct_characters)

        for character_index, character in enumerate(datastream_buffer, start=1):
            if len(window) == window.maxlen:
                window.popleft()

            window.append(character)

            if len(set(window)) == window.maxlen:
                return character_index

        return -1

    @staticmethod
    def parse(puzzle_input: str) -> str:
        """Parse input for puzzle 6.

        :param puzzle_input: Input to parse.
        :return: The datastream buffer received by the device.
        """
        return puzzle_input

    @staticmethod
    def part1(parsed_input: str) -> int:
        """Solves part 1.

        :param parsed_input: The datastream buffer received by the device.
        :return: The number of characters that need to be processed before the
            start-of-packet marker is detected.
        """
        return Day6._get_marker(parsed_input, 4)

    @staticmethod
    def part2(parsed_input: str) -> int:
        """Solves part 2.

        :param parsed_input: The datastream buffer received by the device.
        :return: The number of characters that need to be processed before the
            start-of-message marker is detected.
        """
        return Day6._get_marker(parsed_input, 14)
