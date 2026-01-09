# 11. The Batcomputer: Automation with OS & Sys

> "I'm not doing that by hand." - Every Programmer

Your computer is your domain. You should be able to control files, folders, and paths automatically. We use the `os` and `shutil` modules.

## 1. Where Am I? (Navigation)
```python
import os

cwd = os.getcwd() # Current Working Directory
print(f"You are here: {cwd}")
```

## 2. Listing Files (Scanning the Area)
```python
files = os.listdir()
print(files)
```

## 3. Creating Folders (Building Infrastructure)
```python
if not os.path.exists("confidential"):
    os.mkdir("confidential")
    print("Folder created.")
else:
    print("Folder already exists.")
```

## 4. Renaming & Moving (Shuffling Assets)
```python
# Rename
# os.rename("old_name.txt", "new_name.txt")
```

For moving files, `shutil` is better.
```python
import shutil

# shutil.move("source.txt", "confidential/source.txt")
```

## 5. Walking the Tree (Deep Scan)
Go through every folder and subfolder. This is powerful.

```python
for root, dirs, files in os.walk("."):
    for name in files:
        if name.endswith(".py"):
            print(f"Found python script: {os.path.join(root, name)}")
```

---
**Next Step:** Connecting to the world (APIs).
