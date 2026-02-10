### 46
print("\n===== 46 ======\n")

def assemble():
    print("Avengers Assemble!")

assemble()

### 47
print("\n===== 47 ======\n")

def greet(name):
    print(f"Hello, {name}.")

greet("Peter")

### 48
print("\n===== 48 ======\n")

def force(mass, accel):
    force = mass * accel
    return force

print(force(10,9.8))

### 49
print("\n===== 49 ======\n")

def team_roles(leader, heavy, tech):
    print(f"Team: {leader}, {heavy}, {tech}")

team_roles("Cap", "Hulk", "Iron Man")

### 50
print("\n===== 50 ======\n")

def recruit(hero, sidekick="Robin"):
    print(f"{hero} and {sidekick}.")

recruit("Batman")

### 51
print("\n===== 51 ======\n")

def plan(b="Attack", a="Defend"):
    print(a)
    print(b)

plan()

### 52
print("\n===== 52 ======\n")

x = "Global"

def check_scope():
    print(x)

check_scope()

### 53
print("\n===== 53 ======\n")

def check_pulse(bpm):
    return bpm > 0

print(check_pulse(72))

### 54
print("\n===== 54 ======\n")

def status():
    """Prints status."""
    
print(status.__doc__)

### 55
print("\n===== 55 ======\n")

def add_power(a: int, b: int) -> int:
    return sum

### 56
print("\n===== 56 ======\n")

def team_up(*heroes):
    for hero in heroes:
        print(hero)

team_up("Iron Man", "Thor", "Hulk")

### 57
print("\n===== 57 ======\n")

def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(Name="Stark", Armor="Mk85")

### 58
print("\n===== 58 ======\n")

double = lambda x: x * 2
print(double(5))

### 59
print("\n===== 59 ======\n")

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))

### 60
print("\n===== 60 ======\n")

def backup():
    print("Fighting...")

def fight():
    backup()
    print("Backup arrived!")

fight()