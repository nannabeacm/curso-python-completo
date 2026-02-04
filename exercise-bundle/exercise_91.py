### 91
print("\n===== 91 ======\n")

inventory = {}
asking = True

while asking:
    ask_user = input("Do you wish to view inventory, add item to inventory or exit? [view/add/exit]  ")
    if ask_user == "view":
        print(inventory)
    elif ask_user == "add":
        items = input("What item do you wish to add to inventory? ")
        quantity = input("What's the quantity of the item? ")
        inventory[items] = quantity
        print(inventory)
    else:
        asking = False
        print("Exiting...")