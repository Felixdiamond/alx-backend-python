#!/usr/bin/env python3
"""Define a type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of integers and floats as an argument and returns their sum as a float."""
    return sum(mxd_lst)
