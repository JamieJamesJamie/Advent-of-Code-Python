"""Solutions for day 11."""

# pylint: disable=too-few-public-methods,too-many-arguments


import logging
import math
from collections.abc import Callable, Iterable, Sequence
from operator import add, mul
from typing import Any

from parse import findall, parse, search

from advent_of_code_2022.helper.solver import Solver


class Logger:
    """Logger for debugging."""

    current_round: int
    rounds_to_log: set[int]

    @staticmethod
    def debug(msg: object, *args: object, **kwargs) -> None:
        """Logs a debug message if the :code:`current_round` is in
        :code:`rounds_to_log`.

        :param msg: The message to log.
        :param args: Positional arguments to pass to :code:`logging.debug`.
        :param kwargs: Keyword arguments to pass to :code:`logging.debug`.
        """
        if Logger.current_round in Logger.rounds_to_log:
            logging.debug(msg, *args, **kwargs)


class Monkey:
    """A representation of a monkey."""

    POSSIBLE_OPERATIONS: dict[str, tuple[Callable[[Any, Any], Any], str]] = {
        "*": (mul, "is multiplied"),
        "+": (add, "increases"),
    }

    def __init__(
        self,
        index: int,
        items: list[int],
        operation_string: str,
        divisible_by_operand: int,
        to_monkey_true: int,
        to_monkey_false: int,
    ):
        """Initialises an instance of :code:`Monkey`.

        :param index: The index of the monkey.
        :param items: The list of worry levels for each item the monkey is currently
            holding in the order they will be inspected.
        :param operation_string: A string ending with the format
            new = old <operator> <operand>
        :param divisible_by_operand: The number the worry level must be divisible by to
            satisfy :code:`to_monkey_true`. Otherwise, :code:`to_monkey_false` is
            satisfied.
        :param to_monkey_true: The monkey to throw an item to if the item is divisible
            by :code:`divisible_by_operand`.
        :param to_monkey_false: The monkey to throw an item to if the item is not
            divisible by :code:`divisible_by_operand`.
        """
        self.index: int = index
        self.items: list[int] = items

        self.get_next_monkey = self._operation_function(operation_string)

        self.divisible_by_operand: int = divisible_by_operand
        self.to_monkey: dict[bool, int] = {True: to_monkey_true, False: to_monkey_false}

        self.num_inspections = 0

    def _operation_function(self, line: str) -> Callable[[int, int], int]:
        operation_key, operand = line.split()[-2:]
        operation_function, worry_level_modifier = Monkey.POSSIBLE_OPERATIONS[
            operation_key
        ]

        def _monkey_do(worry_level_divisor: int, modulo: int) -> int:
            old_worry_level = self.items[0]
            Logger.debug(
                "Monkey inspects an item with a worry level of %d", old_worry_level
            )

            self.num_inspections += 1

            int_operand = int(operand) if operand.isdigit() else old_worry_level
            new_worry_level = operation_function(old_worry_level, int_operand)

            self.items[0] = new_worry_level
            Logger.debug(
                "Worry level %s by %d to %d",
                worry_level_modifier,
                int_operand,
                new_worry_level,
            )

            self.items[0] = (self.items[0] // worry_level_divisor) % modulo
            Logger.debug(
                "Monkey gets bored with item. Worry level is divided by %d to %d",
                worry_level_divisor,
                self.items[0],
            )

            test_result = self.items[0] % self.divisible_by_operand == 0

            Logger.debug(
                "Current worry level is%s divisible by %d.",
                "" if test_result else " not",
                self.divisible_by_operand,
            )

            return self.to_monkey[test_result]

        return _monkey_do


class Day11(Solver):
    """Solver for day 11."""

    @staticmethod
    def _calculate_monkey_business(monkey_inspections: Iterable[int]) -> int:
        return mul(*sorted(monkey_inspections, reverse=True)[:2])

    @staticmethod
    def _monkey_do(
        monkey_data: Sequence[Monkey],
        num_rounds: int,
        worry_level_divisor: int,
    ) -> int:
        lowest_common_multiple = math.prod(
            monkey.divisible_by_operand for monkey in monkey_data
        )

        for round_i in range(1, num_rounds + 1):
            Logger.current_round = round_i
            Logger.debug(f"round: {round_i}\n")

            for monkey_index, monkey in enumerate(monkey_data):
                Logger.debug(f"Monkey: {monkey_index}\n")

                for _ in range(len(monkey.items)):
                    next_monkey_index = monkey.get_next_monkey(
                        worry_level_divisor, lowest_common_multiple
                    )
                    item = monkey.items.pop(0)
                    monkey_data[next_monkey_index].items.append(item)
                    Logger.debug(
                        "Item with worry level %d is thrown to monkey %d.\n",
                        item,
                        next_monkey_index,
                    )

            Logger.debug(
                "worry levels:\n%s",
                "\n".join(
                    f"Monkey {monkey_index}: {monkey.items}"
                    for monkey_index, monkey in enumerate(monkey_data)
                ),
            )

        monkey_inspections = tuple(monkey.num_inspections for monkey in monkey_data)
        Logger.debug("Number of inspections each monkey made:\n%s", monkey_inspections)

        return Day11._calculate_monkey_business(monkey_inspections)

    @staticmethod
    def parse(puzzle_input: str) -> tuple[Monkey, ...]:
        monkeys = []

        for monkey_note in puzzle_input.split("\n\n"):
            monkey_lines = monkey_note.split("\n")
            monkeys.append(
                Monkey(
                    parse("Monkey {:d}:", monkey_lines[0])[0],
                    list(item[0] for item in findall("{:d}", monkey_lines[1])),
                    monkey_lines[2],
                    search("Test: divisible by {:d}", monkey_lines[3])[0],
                    search("If true: throw to monkey {:d}", monkey_lines[4])[0],
                    search("If false: throw to monkey {:d}", monkey_lines[5])[0],
                )
            )

        return tuple(monkeys)

    @staticmethod
    def part1(parsed_input: Sequence[Monkey]) -> int:
        max_rounds = 20
        Logger.rounds_to_log = set(range(1, max_rounds + 1))
        return Day11._monkey_do(parsed_input, max_rounds, 3)

    @staticmethod
    def part2(parsed_input: Sequence[Monkey]) -> int:
        max_rounds = 10_000
        Logger.rounds_to_log = {
            1,
            20,
            1_000,
            2_000,
            3_000,
            4_000,
            5_000,
            6_000,
            7_000,
            8_000,
            9_000,
            10_000,
        }
        return Day11._monkey_do(parsed_input, max_rounds, 1)
