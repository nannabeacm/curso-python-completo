# Exercises: Virtual Environments (The Multiverse)

## Mission 1: Create the Universe
Open your terminal inside a *test* folder (create a new empty folder on your desktop called `test_universe` if you want, or just do it in the course folder but don't delete important stuff).
Run the command to **create** a virtual environment named `.venv`.

## Mission 2: Step Through
**Activate** the environment.
Verify it is active (look for the `(.venv)` in your prompt).

## Mission 3: Install a Weapon
While active, install the `colorama` library.
```bash
pip install colorama
```

## Mission 4: Use the Weapon
Create `colored_text.py`.
```python
from colorama import Fore, Style

print(Fore.RED + "This is Red Text like Scarlet Witch magic!" + Style.RESET_ALL)
print("Back to normal.")
```
Run it. It should work ONLY when the venv is active.

## Mission 5: The Snapshot
Generate a `requirements.txt` file using `pip freeze`.
Open the text file to see `colorama` listed there.
