#!/usr/bin/env python3
"""Define a type-annotated function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences as argument and returns a list of tuples."""
    return [(i, len(i)) for i in lst]
