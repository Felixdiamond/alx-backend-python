#!/usr/bin/env python3
"""Module for creating an asyncio.Task from the wait_random function"""
import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio.Task from the wait_random function
    Args:
        max_delay (int): The max delay passed to wait_random
    Returns:
        asyncio.Task: The created Task object
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
