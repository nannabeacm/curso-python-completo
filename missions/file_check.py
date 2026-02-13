try:
    stone_file = open("missing_infinity_stone.txt", "r")
except FileNotFoundError:
    print("Stone not found in this timeline.")
else:
    for line in stone_file:
        print(line)