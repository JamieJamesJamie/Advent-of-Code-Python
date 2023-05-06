"""Solutions for day 11."""


import logging
import math
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from operator import add, mul
from typing import Any, ClassVar

from parse import findall, parse, search

from advent_of_code_2022.helper.solver import Solver


class Logger:
    """
    Logger for debugging.
    """

    # pylint: disable=too-few-public-methods

    current_round: int
    rounds_to_log: set[int]

    @staticmethod
    def debug(msg: object, *args: object, **kwargs) -> None:
        """
        Logs a debug message if the :code:`current_round` is in :code:`rounds_to_log`.

        :param msg: The message to log.
        :param args: Positional arguments to pass to :code:`logging.debug`.
        :param kwargs: Keyword arguments to pass to :code:`logging.debug`.
        """
        if Logger.current_round in Logger.rounds_to_log:
            logging.debug(msg, *args, **kwargs)


@dataclass
class Operator:
    """
    Representation of an operator for a monkey's operation.
    """

    func: Callable[[Any, Any], Any]
    log: str


@dataclass
class Monkey:
    """
    Representation of a monkey.
    """

    POSSIBLE_OPERATORS: ClassVar[dict[str, Operator]] = {
        "*": Operator(mul, "is multiplied"),
        "+": Operator(add, "increases"),
    }

    num_inspections: int = field(default=0, init=False)

    _index: int
    items: list[int]
    _operation_operator: Operator
    _operation_operand: str
    divisible_by_operand: int
    _to_monkey: dict[bool, int]

    def get_next_monkey(self, worry_level_divisor: int, modulo: int) -> int:
        """
        Gets the next :class:`Monkey` index.

        :param worry_level_divisor: Integer to divide new worry level by.
        :param modulo: Maximum worry level allowed.
        :return: The index of the monkey to throw the current item to.
        """

        old_worry_level = self.items[0]
        Logger.debug(
            "Monkey inspects an item with a worry level of %d", old_worry_level
        )

        self.num_inspections += 1

        int_operand = (
            int(self._operation_operand)
            if self._operation_operand.isdigit()
            else old_worry_level
        )
        new_worry_level = self._operation_operator.func(old_worry_level, int_operand)

        self.items[0] = new_worry_level
        Logger.debug(
            "Worry level %s by %d to %d",
            self._operation_operator.log,
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

        return self._to_monkey[test_result]


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
            operation_key, operand = monkey_lines[2].split()[-2:]
            monkeys.append(
                Monkey(
                    parse("Monkey {:d}:", monkey_lines[0])[0],
                    list(item[0] for item in findall("{:d}", monkey_lines[1])),
                    Monkey.POSSIBLE_OPERATORS[operation_key],
                    operand,
                    search("Test: divisible by {:d}", monkey_lines[3])[0],
                    {
                        True: search("If true: throw to monkey {:d}", monkey_lines[4])[
                            0
                        ],
                        False: search(
                            "If false: throw to monkey {:d}", monkey_lines[5]
                        )[0],
                    },
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
