# has_children = True
# print(type(has_children))
# print(has_children.bit_count())
# has_pets = bool(not has_children)
# print(has_pets)

# number_of_children = 5000
# print(type(number_of_children))
# print(number_of_children.bit_count())

# account_balance = 2000.00
# print(account_balance)
# print(type(account_balance))
# print(account_balance.is_integer())
# print(account_balance.hex())

# name = "João"
# print(type(name))
# print(name.count("oã"))

### tuples
planets = ("Mercury", "Venus", "Earth", "Mars","Jupiter", "Saturn", "Uranus", "Neptune")
# print(planets)
# print(type(planets))
# print(planets.index("Jupiter"))

### list
grocery = ["Coffee", "Coffee", "Sugar"]
# grocery = list(planets)
# print(grocery)
# print(type(grocery))
# print(grocery.append("Chantilly"))
# print(grocery)

### sets

ingredients = {"Egg", "Condensed milk", "Egg"}
# print(ingredients)
# print(type(ingredients))

### dictionary

pt_to_en = {
    "oi": "hello",
    "amanhã": "tomorrow",
    "i": "y",
    0: 0
}
print(pt_to_en)

bia_computer = {
    "nickname": "batcomputer",
    "specs": {
        "ram": 64,
        "cpu": 8,
        "storage": 100,
        "has_drive": True,
        "model": "nitro 5"
    }
}
print(bia_computer)
print(type(bia_computer))