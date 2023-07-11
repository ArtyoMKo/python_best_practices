from collections.abc import Sequence
from typing import Iterable

class Items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

def init_sequence(values: Iterable) -> Items:
    return Items(values)
