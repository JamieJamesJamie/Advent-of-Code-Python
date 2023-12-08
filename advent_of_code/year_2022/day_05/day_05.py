"""Solutions for day 5."""


from collections import OrderedDict
from collections.abc import Iterable, Sequence
from typing import NamedTuple

from parse import parse

from advent_of_code.helper.solver import Solver


class Instruction(NamedTuple):
    """Instruction to move crates from one stack to another stack."""

    num_to_move: int
    from_crate: str
    to_crate: str


class SolverState:
    """State of the stacks of crates."""

    # pylint: disable=too-few-public-methods

    instructions: tuple[Instruction, ...]
    stacks: OrderedDict[str, list[str]]

    def __init__(
        self,
        crates: tuple[str, ...],
        stack_labels: tuple[str, ...],
        instructions: tuple[str, ...],
    ):
        """Constructor for :class:`SolverState`.

        :param crates: Lines of crates as described in the input file.
        :param stack_labels: The labels given to stacks in the input
            file.
        :param instructions: The procedure to follow to move crates.
        """
        self.instructions = tuple(
            Instruction(*parse("move {:d} from {} to {}", instruction).fixed)
            for instruction in instructions
        )

        self.stacks = self._parse_crates(crates=crates, stack_labels=stack_labels)

    @staticmethod
    def _parse_crates(
        crates: Iterable[str], stack_labels: Sequence[str]
    ) -> OrderedDict[str, list[str]]:
        """Parse the crate input at the top of the input file.

        :param crates: Lines of crates as described in the input file.
        :param stack_labels: The labels given to stacks in the input
            file.
        :return: A mapping from stack labels to stacks of crates.
        """
        stacks: OrderedDict[str, list[str]] = OrderedDict(
            (stack_label, []) for stack_label in stack_labels
        )

        for line in crates:
            for character_index, character in enumerate(line[1::4]):
                if character.isupper():
                    stacks[stack_labels[character_index]].append(character)

        return stacks

    def top_crates(self) -> str:
        """Returns the top crates from each stack.

        :return: The top crates from each stack.
        """
        return "".join(stack[-1] for stack in self.stacks.values())


class Day5(Solver):
    """Solver for day 5."""

    @staticmethod
    def _parse_instructions_part1(
        instructions: Iterable[Instruction], stacks: OrderedDict[str, list[str]]
    ) -> None:
        """Parse the :param:`instructions` to move crates in the
        :param:`stacks` using the interpretation for part 1 of the puzzle.

        :param instructions: Instructions to move crates in the stacks.
        :param stacks: A mapping from stack labels to stacks of crates.
        """
        for instruction in instructions:
            for _ in range(instruction.num_to_move):
                stacks[instruction.to_crate].append(
                    stacks[instruction.from_crate].pop()
                )

    @staticmethod
    def _parse_instructions_part2(
        instructions: Iterable[Instruction], stacks: OrderedDict[str, list[str]]
    ) -> None:
        """Parse the :param:`instructions` to move crates in the
        :param:`stacks` using the interpretation for part 2 of the puzzle.

        :param instructions: Instructions to move crates in the stacks.
        :param stacks: A mapping from stack labels to stacks of crates.
        """
        for instruction in instructions:
            # Add crates to new stack
            stacks[instruction.to_crate].extend(
                stacks[instruction.from_crate][instruction.num_to_move :]
            )

            # Remove crates from old stack
            stacks[instruction.from_crate] = stacks[instruction.from_crate][
                : instruction.num_to_move
            ]

    @staticmethod
    def parse(puzzle_input: str) -> SolverState:
        """Parse input for puzzle 5.

        :param puzzle_input: Input to parse.
        :return: The state of the puzzle.
        """
        crates, instructions = tuple(
            tuple(line.splitlines()) for line in puzzle_input.split("\n\n")
        )

        solver_state = SolverState(
            crates=crates[-2::-1],
            stack_labels=tuple(crates[-1].split()),
            instructions=instructions,
        )

        return solver_state

    @staticmethod
    def part1(parsed_input: SolverState) -> str:
        """Solves part 1.

        :param parsed_input: The starting arrangement of crate stacks.
        :return: The top crates from each stack.
        """
        Day5._parse_instructions_part1(
            instructions=parsed_input.instructions, stacks=parsed_input.stacks
        )

        return parsed_input.top_crates()

    @staticmethod
    def part2(parsed_input: SolverState) -> str:
        """Solves part 2.

        :param parsed_input: The starting arrangement of crate stacks.
        :return: The top crates from each stack.
        """
        parsed_input.instructions = tuple(
            Instruction(
                num_to_move=-instruction.num_to_move,
                from_crate=instruction.from_crate,
                to_crate=instruction.to_crate,
            )
            for instruction in parsed_input.instructions
        )

        Day5._parse_instructions_part2(
            instructions=parsed_input.instructions, stacks=parsed_input.stacks
        )

        return parsed_input.top_crates()
