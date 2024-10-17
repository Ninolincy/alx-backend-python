#!/usr/bin/env python3

import asyncio
import random


"""
    define an asynchronous coroutine
    that takes in an integer argument
"""


async def wait_random(max_delay: int = 10) -> float:
    """
        waits for a random delay between 0 and max_delay
        seconds and eventually returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
