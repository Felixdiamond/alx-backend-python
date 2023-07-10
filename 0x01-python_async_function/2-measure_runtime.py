#!/usr/bin/env python3
"""Module for measuring the runtime of the wait_n function"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)
    Args:
        n (int): The number of times the wait_random coroutine should

        be called max_delay (int): The max delay passed to wait_random
    Returns:
        float: The total elapsed runtime divided by n
    """
    start_time = time()

    run(wait_n(n, max_delay))

    elapsed = time() - start_time

    return (elapsed) / n
