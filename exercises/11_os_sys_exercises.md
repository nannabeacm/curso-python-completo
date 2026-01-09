# Exercises: OS & Sys (The Batcomputer)

## Mission 1: The Scanner
Create `scanner.py`.
Print the name of your Operating System (`os.name`).
Print the current directory you are in.

## Mission 2: The Organizer
Create `organize.py`.
1. Create a list of dummy file names: `["plan_alpha.txt", "plan_beta.txt", "image.png", "logo.jpg"]`.
2. Create dummy files for them using a loop and `open(name, "w")`.
3. Create two folders: `text_files` and `images`.
4. Loop through the files again.
   - If it ends with `.txt`, move it to `text_files`.
   - If it ends with `.png` or `.jpg`, move it to `images`.
   - *Use `shutil.move`*.

## Mission 3: The Search
Create `search.py`.
Walk through the current directory tree using `os.walk`.
Find ANY file that contains "secret" in its name.
Print the full path to that file.
