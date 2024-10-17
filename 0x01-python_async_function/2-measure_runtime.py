#!/usr/bin/env python3

import asyncio
import time
"""
    import wait_n from 1-concurrent_coroutines
    measure_time function with integers n
    and max_delay as arguments
"""

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        measure the total execution time for wait_n
        and return total time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
