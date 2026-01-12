 # Create sorting_hat.py. 
 # Ask the user "Do you imply bravery? (yes/no)". 
 # If yes, print "Gryffindor!". If no, ask "Are you ambitious? (yes/no)". 
 # If yes, print "Slytherin!". Else, print "Hufflepuff for you!".

imply_bravery = input("Do you imply bravery? (yes/no)\n")

if imply_bravery == "yes":
    print("Gryffindor!")
else:
    is_ambitious = input("Are you ambitious? (yes/no)\n")
    if is_ambitious == "yes":
        print("Slytherin!")
    else: 
        print("Hufflepuff for you!")
    