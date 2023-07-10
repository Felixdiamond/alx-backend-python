#!/usr/bin/env python3
"""Module for creating multiple asyncio.Tasks from the wait_random function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates multiple asyncio.Tasks from the wait_random function and
    returns their results
    Args:
        n (int): The number of Tasks to create
        max_delay (int): The max delay passed to wait_random
    Returns:
        List[float]: The list of results from the created Tasks
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
