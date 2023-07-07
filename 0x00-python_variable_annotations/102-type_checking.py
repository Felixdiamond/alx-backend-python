#!/usr/bin/env python3
"""This module defines a type-annotated function zoom_array that takes a tuple and an int as arguments and returns a list."""

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Takes a tuple lst and an int factor as arguments and returns a list.

    Args:
        lst: A tuple containing the elements to be repeated.
        factor: An int specifying the number of times each element of lst should be repeated. Defaults to 2.

    Returns:
        A list containing each element of lst repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
