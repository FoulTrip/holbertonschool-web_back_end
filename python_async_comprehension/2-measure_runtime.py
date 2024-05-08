#!/usr/bin/env python3
"""from the previous file and write a 
measure_runtime coroutine that will 
execute async_comprehension four times 
in parallel using asyncio.gather."""

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    start_time = time.time()
    execution_time = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*execution_time)

    end_time = time.time()
    return end_time - start_time
