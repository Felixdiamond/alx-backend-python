#!/usr/bin/env python3
"""Define a type-annotated function zoom_array"""
from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Takes a tuple and an int as arguments and returns a list."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
