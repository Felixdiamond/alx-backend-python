#!/usr/bin/env python3
"""This module defines a type-annotated function sum_list that takes a list of floats as an argument and returns their sum as a float."""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats as an argument and returns their sum as a float.

    Args:
        input_list: A list of floats.

    Returns:
        The sum of the elements in input_list as a float.
    """
    return sum(input_list)
