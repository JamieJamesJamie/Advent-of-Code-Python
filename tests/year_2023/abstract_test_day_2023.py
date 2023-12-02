"""Abstract test class to be used for testing Solution classes for the year
2023."""


from abc import ABCMeta

from tests.helper.abstract_test_day import AbstractTestDay


class AbstractTestDay2023(AbstractTestDay, metaclass=ABCMeta):
    """Abstract class to be used for testing solutions for the year 2023."""

    @staticmethod
    def year() -> int:
        return 2023
