"""Abstract test class to be used for testing Solution classes for the year
2024."""

from abc import ABCMeta

from tests.helper.abstract_test_day import AbstractTestDay


class AbstractTestDay2024(AbstractTestDay, metaclass=ABCMeta):
    """Abstract class to be used for testing solutions for the year 2024."""

    @staticmethod
    def year() -> int:
        return 2024
