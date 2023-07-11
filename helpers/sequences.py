from collections.abc import Sequence
from typing import Iterable


class Items(Sequence):
    """Custom sequence"""

    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)


def init_sequence(values: Iterable) -> Items:
    # pylint: disable=missing-function-docstring
    return Items(values)
