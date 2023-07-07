#!/usr/bin/env python3
"""This module defines a type-annotated function element_length that takes an iterable of sequences as argument and returns a list of tuples."""

from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences as argument and returns a list of tuples.

    Args:
        lst: An iterable of sequences.

    Returns:
        A list of tuples containing each element of lst as the first element and the length of that element as the second element.
    """
    return [(i, len(i)) for i in lst]
