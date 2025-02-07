#!/usr/bin/env python3

import asyncio
"""
    function that takes an integer max_delay
    returns a asyncio.Task
"""

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:

    task = asyncio.create_task(wait_random(max_delay))
    return task
