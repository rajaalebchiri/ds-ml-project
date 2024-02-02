#!/usr/bin/env python
# asynchro.py
import asyncio
import time


async def count():
    """async function sleep for 1 second"""
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    """gather async functions"""
    await asyncio.gather(count(), count(), count())


async def say_after(delay, what):
    """async hello world func"""
    await asyncio.sleep(delay)
    print(what)


async def run_main():
    """Simple coroutine"""
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "hello")
    await say_after(2, "world")
    print(f"finished at {time.strftime('%X')}")


async def run_main_create_task():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"main() executed in {elapsed:0.2f} seconds.")
    asyncio.run(run_main())
