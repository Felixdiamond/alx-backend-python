#!/usr/bin/env python3
"""Module for measuring the runtime of the wait_n function"""
import time
wait_n = __import__('2-measure_runtime').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): The number of times to call wait_n
        max_delay (int): The maximum delay for each call to wait_n

    Returns:
        float: The average time per call to wait_n
    """
    start = time.time()
    wait_n(n, max_delay)
    total_time = time.time() - start
    return total_time / n
