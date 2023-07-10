#!/usr/bin/env python3
"""Module for measuring the runtime of the wait_n function"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)
    Args:
        n (int): The number of times the wait_random coroutine should be
        called max_delay (int): The max delay passed to wait_random
    Returns:
        float: The total elapsed runtime divided by n
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return (elapsed / 2)
