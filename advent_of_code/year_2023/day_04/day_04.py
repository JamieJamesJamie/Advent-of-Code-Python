"""Solutions for day 4."""


from collections.abc import Iterable, Sequence

from advent_of_code.helper.solver import Solver


class Day4(Solver):
    """Solver for day 4."""

    @staticmethod
    def parse(puzzle_input: str) -> tuple[int, ...]:
        """
        Parse input for puzzle 4.

        :param puzzle_input: Input to parse.
        :return: The number of matches for each card.
        """
        return tuple(
            len(
                set.intersection(
                    *(
                        {int(number) for number in numbers.split()}
                        for numbers in line.split(":")[1].split("|")
                    )
                )
            )
            for line in puzzle_input.splitlines()
        )

    @staticmethod
    def part1(parsed_input: Iterable[int]) -> int:
        """
        Solves part 1.

        :param parsed_input: The number of matches for each card.
        :return: The total number of points from each card.
        """
        return sum(int(2 ** (matches - 1)) for matches in parsed_input)

    @staticmethod
    def part2(parsed_input: Sequence[int]) -> int:
        """
        Solves part 2.

        :param parsed_input: The number of matches for each card.
        :return: The total number of cards that have been won.
        """
        num_cards = [1] * len(parsed_input)

        for card_index, num_of_card_index in enumerate(num_cards):
            for num_forward in range(1, parsed_input[card_index] + 1):
                num_cards[card_index + num_forward] += num_of_card_index

        return sum(num_cards)
