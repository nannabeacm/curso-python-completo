# Exercises: AsyncIO (The Speed Force)

## Mission 1: The Race
Create `race.py`.
1. Define an async function `racer(name, delay)`.
   - Print `"{name} started!"`.
   - `await asyncio.sleep(delay)`.
   - Print `"{name} finished!"`.
2. Create `main()`.
   - Run two racers: "Flash" (1 second) and "Superman" (1.5 seconds) using `gather`.
3. Run `asyncio.run(main())`.

## Mission 2: Multi-Download Simulation
Create `download.py`.
1. Defines `download_file(file_name)`.
   - Print "Downloading {file_name}..."
   - Sleep for 2 seconds.
   - Print "Downloaded {file_name}."
2. In `main`, download 3 files ("Data1", "Data2", "Data3") concurrently.
   - Observe that they all start continuously without waiting for the previous one to finish.
