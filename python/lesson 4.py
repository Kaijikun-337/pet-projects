import asyncio
import time

# 1. Make this async
async def brew_coffee(name):
    print(f"☕ Starting {name}...")
    await asyncio.sleep(2)
    
    print(f"✅ {name} ready!")

async def main():
    start = time.time()
    
    # 3. Run all 3 orders AT THE SAME TIME
    # Hint: await asyncio.gather(func1, func2, func3)
    await asyncio.gather(
        brew_coffee("Order 1"),
        brew_coffee("Order 3"),
        brew_coffee("Order 4"),
        brew_coffee("Order 2")
    )
    
    print(f"Total time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())