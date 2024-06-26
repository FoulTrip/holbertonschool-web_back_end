#!/usr/bin/env python3
"""wait_n should return the list of all
the delays (float values). The list of
the delays should be in ascending order
without using sort() because of concurrency."""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random coroutine 'n' times"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
