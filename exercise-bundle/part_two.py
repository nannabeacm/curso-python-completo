### 16
print("\n===== 16 ======\n")

object_seen = "Superman"

if object_seen == "Superman":
    print("It's a bird! It's a plane! It's Superman!")

### 17
print("\n===== 17 ======\n")

alingment = "Villain"

if alingment == "Hero":
     print("Save the cat.")
else: 
     print("Destroy the world.")

### 18
print("\n===== 18 ======\n")

threat_level = 9

if threat_level < 5:
    print("street level")
elif threat_level >= 5 and threat_level < 8:
    print("city level")
else:
    print("avengers level")

### 19
print("\n===== 19 ======\n")

thor = 100
hulk = 110

if hulk > thor:
    print("Hulk is stronger")

### 20
print("\n===== 20 ======\n")

ask_for_password = input("Enter password: ")

if ask_for_password == "Cap":
    print("Access Granted")
else:
    print("Access Denied")

### 21
print("\n===== 21 ======\n")

is_noble = True
is_strong = True

if is_noble and is_strong:
    print("Worthy of Mjolnir")

### 22
print("\n===== 22 ======\n")

has_shield = False
has_hammer = True

if has_shield or has_hammer:
    print("Ready for battle")

### 23
print("\n===== 23 ======\n")

button_pressed = False

if not button_pressed:
    print("Safe")

### 24
print("\n===== 24 ======\n")

ask_for_level = int(input("Insert level: "))

if ask_for_level > 5:
    what_code = input("Insert Code: ")
    if what_code == "Alpha":
        print("\nWelcome Director Fury.")
    else:
        print("\nAccess Denied.")

### 25
print("\n===== 25 ======\n")

team = "Iron Man, Thor, Hulk"

print("Thor" in team)

### 26
print("\n===== 26 ======\n")

name = ""

# if name != "" and name is not None:
if name:
    print("Name exists.")
else:
    print("No name provided.")

### 27
print("\n===== 27 ======\n")

status = ""
energy = 50

if energy > 0:
    status = "Online"
else:
    status = "Offline"

print(status)

### 28
print("\n===== 28 ======\n")

speed = int(input("What's the speed? "))

if speed > 88:    
    print("Time Travel Imminent.")

### 29
print("\n===== 29 ======\n")

card = "Ace"

if card != "Joker":
    print("Safe")

### 30
print("\n===== 30 ======\n")

missions_completed = 7

if missions_completed > 10:
    print("Pro")
elif missions_completed > 5:
    print("Intermediate") 
else:
    print("Rookie")