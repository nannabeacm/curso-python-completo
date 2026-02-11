### 81
print("\n===== 81 ======\n")

# .csv - Comma (,) separated values

file_data = "Stark,100"

with open("data.txt", "w") as f:
    f.write(file_data)

with open("data.txt", "r") as f:
    print(f.read().split(",")[0])

### 82
print("\n===== 82 ======\n")

hero_list = ["Hulk", "Thor"]

with open("team.txt", "w") as f:
    for item in hero_list:
        f.write(f"{item}\n")


### 83
print("\n===== 83 ======\n")

with open("team.txt", 'r') as f:
    lines = len(f.readlines())
    print(lines)

### 84
print("\n===== 84 ======\n")

with open("team.txt", "r") as f:
    content = f.read()

print("Hulk" in content)

### 85
print("\n===== 85 ======\n")

with open("mission.txt", "r") as f:
    content = f.read()

with open("backup_mission.txt", "w") as f:
    f.write(content)

### 86
print("\n===== 86 ======\n")

try:
    with open("ghost.txt", "r") as file:
        content = file.read()
        # if not "," in line:
        #     raise NotACSVFile
        print(content)
except FileNotFoundError:
    print("File not found.")
# except NotACSVFile:
#     print("Hold on!!! Give me a CSV file!")

### 87
print("\n===== 87 ======\n")

with open("team.txt", "r") as f:
    names = f.read().splitlines()

names.sort()

print(names)

### 88
print("\n===== 88 ======\n")

data_message = " Data \n"

with open("clean_data.txt", "w") as f:
    f.write(data_message)

with open("clean_data.txt", "r") as f:
    line = f.read()

clean_line = line.strip()
print(clean_line)

### 89
print("\n===== 89 ======\n")

import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

date_and_time = f"{current_time} - Event"

with open("time_and_date.txt", "w") as f:
    f.write(date_and_time)

with open("time_and_date.txt", "r") as f:
    content = f.read()
    print(content)

### 90
print("\n===== 90 ======\n")

config_message = "difficulty=hard"

with open("config.txt", "w") as f:
    f.write(config_message)

with open("config.txt", "r") as f:
    content = f.read().strip()

key, value = content.split("=")

print(value)
