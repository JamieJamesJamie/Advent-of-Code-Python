"""Helper functions that may be useful to solve some Advent of Code
problems."""


def inclusive_range(start, stop=None, step=1):
    """
    Return an object that produces a sequence of integers from
    :param:`start` (inclusive) to :param:`stop` (inclusive) by :param:`step`.

    range(i, j) produces i, i+1, i+2, ..., j.

    range(i) produces 0, 1, 2, ..., i.

    When :param:`step` is given, it specifies the increment (or decrement).

    :param start: The starting number.
    :param stop: The inclusive stopping number.
    :param step: The increment or decrement.
    :return: An inclusive range.
    """
    return range(start + 1) if stop is None else range(start, stop + 1, step)
