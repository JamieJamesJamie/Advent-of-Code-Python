"""Solutions for day 10."""

import os
from collections.abc import Iterator

from advent_of_code_ocr import convert_6

from advent_of_code.helper.solver import Solver


class Day10(Solver):
    """Solver for day 10."""

    @staticmethod
    def parse(puzzle_input: str) -> Iterator[tuple[str, ...]]:
        """Parse input for puzzle 10.

        :param puzzle_input: Input to parse.
        :return: A sequence of CPU instructions.
        """
        return (tuple(line.split()) for line in puzzle_input.splitlines())

    @staticmethod
    def part1(parsed_input: Iterator[tuple[str, ...]]) -> int:
        """Solves part 1.

        :param parsed_input: A sequence of CPU instructions.
        :return: The sum of the 20th, 60th, 100th, 140th, 180th and
            220th CPU cycles.
        """
        register_x = 1
        cycles_until_free = 0
        operand = 0
        max_cycle = 220
        interesting_cycles = {
            interesting_cycle: 0 for interesting_cycle in range(20, max_cycle + 1, 40)
        }

        for cycle_number in range(1, max_cycle + 1):
            if cycle_number in interesting_cycles:
                interesting_cycles[cycle_number] = register_x

            if cycles_until_free == 0:
                try:
                    instruction = next(parsed_input)
                except StopIteration:
                    break

                if instruction[0] == "noop":
                    # noop
                    pass
                else:
                    # addx
                    cycles_until_free = 1
                    operand = int(instruction[1])

            else:
                cycles_until_free -= 1
                register_x += operand

            # print(f"cycle number: {cycle_number}")
            # print(f"X: {register_x}")

        signal_strengths = {
            interesting_cycle: interesting_cycle * interesting_cycles[interesting_cycle]
            for interesting_cycle in interesting_cycles
        }

        return sum(signal_strengths.values())

    @staticmethod
    def part2(parsed_input: Iterator[tuple[str, ...]]) -> str:
        """Solves part 2.

        :param parsed_input: A sequence of CPU instructions.
        :return: The rendered image given by the CPU instructions. If
            the rendered image can be converted to text using an OCR,
            then this is appended to the end of the puzzle answer.
        """
        # The X (register_x) position controls the horizontal position of a sprite.

        # The sprite is 3 pixels wide, and the X position corresponds to the middle
        # pixel in that sprite.

        # If the sprite is positioned such that 1 of its 3 pixels is the pixel currently
        # being drawn, the screen produces a lit pixel (#).
        # Otherwise, the screen leaves the pixel dark (.).

        crt_screen = ""
        register_x = 1
        cycles_until_free = 0
        operand = 0
        max_width = 40
        max_height = 6

        for position_vertical in range(max_height):
            if position_vertical != 0:
                crt_screen += os.linesep

            for position_horizontal in range(max_width):
                # Draw stuff here
                crt_screen += (
                    "#"
                    if position_horizontal in range(register_x - 1, register_x + 2)
                    else "."
                )

                if cycles_until_free == 0:
                    try:
                        instruction = next(parsed_input)
                    except StopIteration:
                        break

                    if instruction[0] == "noop":
                        # noop
                        pass
                    else:
                        # addx
                        cycles_until_free = 1
                        operand = int(instruction[1])

                else:
                    cycles_until_free -= 1
                    register_x += operand

        try:
            crt_screen_string = convert_6("\n".join(crt_screen.split(os.linesep)))
        except (KeyError, ValueError):
            crt_screen_string = ""

        return (
            crt_screen + (os.linesep if crt_screen_string else "") + crt_screen_string
        )
