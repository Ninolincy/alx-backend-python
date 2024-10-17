#!/usr/bin/env python3

import asyncio
"""
    an async routine called task_wait_n
    that takes in 2 int arguments:
"""

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> float:
    """
        spawn wait_random n times with the specified max_delay
        and return the list of all the delays
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
