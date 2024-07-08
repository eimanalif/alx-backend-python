#!/usr/bin/env python3
'''task01
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:int, max_delay:int)-> List[float]:
    '''excuting wait_n
    '''
    wait_times = await asyncio.gather(*tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(wait_times)
