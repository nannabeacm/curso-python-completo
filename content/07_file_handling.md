# 07. The Archives: File Handling

> "The files are in the computer." - Zoolander (Wait, wrong universe).
> "Secrets have a weight. The more you keep, the harder it is to move." - Natasha Romanoff

Programs need to save data. You can't just keep everything in RAM (Memory), because when you close the program (or the multiverse resets), it's gone. We need to write to **Files**.

## 1. Opening a File (`open`)
Used to open a file.
Modes:
- `"r"`: Read (Default).
- `"w"`: Write (Overwrites everything).
- `"a"`: Append (Adds to the end).

## 2. Reading
The `with` statement is your safety net. It automatically closes the file even if errors happen (like a self-destruct mechanism).

```python
# Reading the Hydra protocol
try:
    with open("hydra_secrets.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File missing. Fury might have deleted it.")
```

## 3. Writing
WARNING: `"w"` wipes the file clean.

```python
mission_report = "Mission Report: December 16, 1991."

with open("report.txt", "w") as f:
    f.write(mission_report)
```

## 4. Appending
Add to the log without deleting history.

```python
log_entry = "\nUpdate: Target neutralized."

with open("report.txt", "a") as f:
    f.write(log_entry)
```

---
**Next Step:** Handling explosions (Errors).
