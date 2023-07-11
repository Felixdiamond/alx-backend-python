#!/usr/bin/env python3
"""This module defines a coroutine that measures the runtime of
async_comprehension.

The measure_runtime coroutine executes the async_comprehension
coroutine four times in parallel using asyncio.gather. The total runtime
is measured and returned.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure and return the total runtime of executing async_comprehension
    four times.

    This coroutine uses asyncio.gather to execute the async_comprehension
    coroutine four times in parallel. The total runtime is measured using
    the time module and returned as a float.

    Returns:
        float: The total runtime of executing async_comprehension four times.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
