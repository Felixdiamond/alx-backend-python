#!/usr/bin/env python3
"""Define a type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int or float v as arguments and returns a tuple."""
    return k, float(v) ** 2
