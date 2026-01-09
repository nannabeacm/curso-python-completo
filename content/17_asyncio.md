# 17. The Speed Force: AsyncIO

> "My name is Barry Allen, and I am the fastest man alive." - The Flash

Normal Python is Synchronous. It waits for one thing to finish before starting the next.
**AsyncIO** allows you to do multiple things while waiting (Concurreny).

## 1. Sync vs Async
- **Sync:** Order coffee. Wait. Get coffee. Order Toast. Wait. Get Toast. (Slow).
- **Async:** Order coffee. Order Toast. Check Phone. Get Coffee. Get Toast. (Fast).

## 2. Coroutines (`async def`)
You define an async function with `async def`. You call it with `await`.

```python
import asyncio

async def run_fast():
    print("Start running...")
    await asyncio.sleep(1) # Simulates waiting for I/O (Database, API)
    print("Finished lap.")

# You cannot just call run_fast(). You need an event loop.
# asyncio.run(run_fast())
```

## 3. Running concurrently (`gather`)
The true power.

```python
import asyncio

async def save_civilian(name, time_needed):
    print(f"Saving {name}...")
    await asyncio.sleep(time_needed)
    print(f"Saved {name}!")

async def main():
    # Run these at the SAME TIME
    await asyncio.gather(
        save_civilian("Mary Jane", 2),
        save_civilian("Gwen Stacy", 2),
        save_civilian("Aunt May", 1)
    )

if __name__ == "__main__":
    asyncio.run(main())
```

In the Sync world, this would take 2+2+1 = 5 seconds.
In Async, it takes max(2, 2, 1) = 2 seconds. You just saved 3 seconds (and Gwen Stacy).

---
**Congratulations!** You have completed the Advanced Python Course.
You are now an Avenger level developer.
