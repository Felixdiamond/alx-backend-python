#!/usr/bin/env python3
"""Example script that uses the async_generator coroutine"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that yields random numbers between 0 and 10"""
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
