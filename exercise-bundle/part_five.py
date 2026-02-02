### 61
print("\n===== 61 ======\n")

heroes = ["Iron Man", "Cap"]

print(heroes)

### 62
print("\n===== 62 ======\n")

print(heroes[0])

### 63
print("\n===== 63 ======\n")

heroes.append("Spider-Man")

print(heroes)

### 64
print("\n===== 64 ======\n")

heroes.remove("Cap")

print(heroes)

### 65
print("\n===== 65 ======\n")

all_heroes = ["A", "B", "C", "D"]

team_a = all_heroes[0:2]

print(team_a)

### 66
print("\n===== 66 ======\n")

stats = {
    "strength": 100,
    "speed": 50
}

print(stats)

### 67
print("\n===== 67 ======\n")

print(stats["strength"])

### 68
print("\n===== 68 ======\n")

stats["speed"] = 60

stats["intellect"] = 90

print(stats)

### 69
print("\n===== 69 ======\n")

for key, value in stats.items():
        print(f"{key}: {value}")

### 70
print("\n===== 70 ======\n")

new_list = ["Fly", "Run", "Fly"]

print(new_list)

new_list_set = set(new_list)

print(new_list_set)

### 71
print("\n===== 71 ======\n")

batman_enemies = {"Joker", "Bane"}
superman_enemies = {"Lex", "Joker"}

mutual_enemies = batman_enemies.intersection(superman_enemies)

print(mutual_enemies)

### 72
print("\n===== 72 ======\n")

loc = (10, 20)

print(loc)

### 73
print("\n===== 73 ======\n")

x, y = loc

print(x)

### 74
print("\n===== 74 ======\n")

db = [{"name": "Stark"}, {"name": "Rogers"}]

print(db[1]["name"])

### 75
print("\n===== 75 ======\n")

teams = {"Avengers": ["Thor", "Hulk"], "X-Men": ["Wolverine"]}

print(teams["Avengers"][0])

### 76
print("\n===== 76 ======\n")

mission_message = "Save the world"

with open("mission.txt", "w") as f:
    f.write(mission_message)

with open("mission.txt", "r") as f:
    content = f.read()
    print(content)

### 77
print("\n===== 77 ======\n")

with open("lines.txt", "r") as f:
    lines = f.readlines()
    print(lines)

### 78
print("\n===== 78 ======\n")

file_message = "Mission Success"

with open("log.txt", "w") as f:
    f.write(file_message)

### 79
print("\n===== 79 ======\n")

file_append = "\nReturn to base"

with open("log.txt", "a") as f:
    f.write(file_append)

# 80. Safe Open (With)
# Difficulty: Easy Mission: Use with open(...) to read log.txt. Print content. Example Output:

# Mission Success
# Return to base

### 80
print("\n===== 80 ======\n")

with open("log.txt", "r") as f:
    content = f.read()
    print(content)