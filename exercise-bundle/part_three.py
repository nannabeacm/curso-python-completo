### 31
print("\n===== 31 ======\n")

number_start = 1

while number_start <= 5:
    print(number_start)
    number_start += 1

### 32
print("\n===== 32 ======\n")

heroes = ["Batman", "Superman", "Wonder Woman"]

for item in heroes:
   print(item)

### 33
print("\n===== 33 ======\n")

countdown = 3

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Liftoff!") 

### 34
print("\n===== 34 ======\n")

hits = [10, 20, 15]
total_damage = 0

for item in hits:
    total_damage += item

print(total_damage)

### 35
print("\n===== 35 =====\n")

people = ["Hero", "Hero", "Spy", "Hero"]

for item in people:
    if "Spy" in people:
        print("Found him!")
    break

### 36
print("\n===== 36 ======\n")

number_count = 0

while number_count < 5:
    number_count += 1
    if number_count == 3:
        continue # why they didn't use "skip" instead?
    print(number_count)

### 37
print("\n===== 37 ======\n")

# Tradução intervalo ou faixa de valores
for i in range(0, 21, 5):
    print(i)

### 38
print("\n===== 38 ======\n")

# implicitly is range(0, 2, 1)
for x in range(2):
    for y in range(2):
        print(f"({x}, {y})")

### 39
print("\n===== 39 ======\n")

secret = 7
guess = None

while guess != secret:
    guess = int(input("Guess: "))
    if guess == secret:
        print("Correct")

### 40
print("\n===== 40 ======\n")

racers = ["Flash", "Quicksilver"]

for position, name in enumerate(racers):
    print(f"{position +1}.", name)

### 41
print("\n===== 41 ======\n")

code = "S.H.I.E.L.D."

for char in code:
    if char != ".":
        print(char, end="")

### 42
print("\n===== 42 ======\n")

reps = 0

while reps < 3:
    print("Lifting...")
    reps += 1

### 43
print("\n===== 43 ======\n")

for i in range(1, 4):
    print(i, i**2)

### 44
print("\n===== 44 ======\n")

char_list = ["Stark", "Thanos", "Rogers"]
found = None

for item in char_list:
    if "Thanos" in char_list:
        found = True
        if found:
            print("Thanos found")
    break

### 45
print("\n===== 45 ======\n")

infinity_stones = ["Stone", "Rock", "Stone", "Gem"]
stone_count = 0

for stone in infinity_stones:
    if stone == "Stone":
        stone_count += 1

print(stone_count)
