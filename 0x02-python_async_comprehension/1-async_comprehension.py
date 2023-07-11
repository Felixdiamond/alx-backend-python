#!/usr/bin/env python3
"""This module defines a coroutine that collects random numbers.

The async_comprehension coroutine collects 10 random numbers from the
async_generator coroutine using an asynchronous comprehension. The collected
random numbers are returned as a list.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect and return 10 random numbers from async_generator.

    This coroutine uses an asynchronous comprehension to collect 10 random
    numbers yielded by the async_generator coroutine. The collected random
    numbers are returned as a list.

    Returns:
        List[float]: A list of 10 random numbers from async_generator.
    """
    result = [i async for i in async_generator()]
    return result
