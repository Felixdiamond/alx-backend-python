#!/usr/bin/env python3
"""Example script that uses the async_generator coroutine"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generate random numbers between 0 and 10.

    This coroutine generates a sequence of 10 random numbers between 0 and 10.
    On each iteration of the loop, the coroutine asynchronously waits for 1
    second before yielding the next random number. The random numbers
    are generated using the uniform function from the random module.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())
