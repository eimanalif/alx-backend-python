#!/usr/bin/env python3
'''task 0'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''a range 0-10 genarator'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
