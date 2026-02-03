### 95
print("\n===== 95 ======\n")

team = []

print("Welcome, Captain America! Today's mission involves STEALTH and HAND-TO-HAND COMBAT.")
ask_user = input("What hero do you wish to take to today's mission? ")
team.append(ask_user)

for i in range(4):
    ask_user_again = input("What other hero do you wish to take to today's mission? ")
    team.append(ask_user_again)

remove_hero = input("ERROR! Only 4 heroes allowed in the team for this mission! Please remove a hero: ")

if remove_hero in team:
    team.remove(remove_hero)

print("TEAM UPDATED. Heroes chosen: ", ', '.join(team))