#!/usr/bin/env python3
"""function’s parameters and return
values with the appropriate types"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function than an iterable object"""

    return [(i, len(i)) for i in lst]
