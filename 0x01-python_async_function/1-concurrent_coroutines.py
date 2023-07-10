#!/usr/bin/env python3
"""Asynchronous coroutine that waits for multiple random delays and returns
them."""

import asyncio
from typing import List
<<<<<<< HEAD
from 0 - basic_async_syntax import wait_random
=======
wait_random = __import__('0-basic_async_syntax').wait_random
>>>>>>> 0ecd31ab2657d3472eb6d854336f769aa67aa4d8


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that waits for n random delays between 0 and
    max_delay seconds and returns them."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
