import asyncio
import time

async def task_a():
    print("🅰️ A: Start")
    print("🅰️ A: Working hard...")
    # This is the HANDOFF point.
    # We yield control to the Event Loop for 1 second.
    time.sleep(1) 
    print("🅰️ A: Resumed! (Database replied)")
    print("🅰️ A: Finish")

async def task_b():
    print("🅱️ B: Start (I was waiting for A to yield!)")
    print("🅱️ B: Working...")
    await asyncio.sleep(1)
    print("🅱️ B: Finish")

async def main():
    print("🔄 LOOP: Starting tasks...")
    # Schedule both, but don't wait for them yet
    t1 = asyncio.create_task(task_a())
    t2 = asyncio.create_task(task_b())
    
    # We are now waiting for the loop to process them
    await t1
    await t2
    print("🔄 LOOP: All done")

if __name__ == "__main__":
    asyncio.run(main())