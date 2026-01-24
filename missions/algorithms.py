## 1. Search
print("===== Search ======")
my_consoles = [ "X-Box", "PS4", "PS5"]

### How to search? Iterate and compare

target = "PS4"

for element in my_consoles:
    if target == element:
        print("I found it!")
        print(element)
        break
    print(f"Looking for my {target}") 


# Grouping
print("\n\n===== Grouping ======")
games_per_console = {}

games = [
    {
        "Title": "Halo",
        "Platform": "X-Box",
        "Rate": 8.0
    },
    {
        "Title": "Half-Life 2",
        "Platform": "X-Box",
        "Rate": 9.5
    },
    {
        "Title": "Marvel's Spider-Man",
        "Platform": "PS4",
        "Rate": 8.0
    },
    {
        "Title": "Street Fighter 5",
        "Platform": "PS4",
        "Rate": 7.5
    },
    {
        "Title": "Little Big Planet 3",
        "Platform": "PS4",
        "Rate": 6.5
    },
    {
        "Title": "Elden Ring",
        "Platform": "PS5",
        "Rate": 10.0
    },
]

for game in games:
    platform = game["Platform"]
    title = game["Title"]
    if not platform in games_per_console.keys():
        games_per_console[platform] = [] # List of games is empty

    games_per_console[platform].append(title)
print("games_per_console", games_per_console)

print("\n\n===== Grouping with count ======")

total_per_console = {}    
for platform in games_per_console:
   if not platform in total_per_console.keys():
      total_per_console[platform] = len(games_per_console[platform])
    
print("total_per_console", total_per_console)

print("\n\n===== Calculating max value ======")

best_game = None # Max is unknow yet

for game in games:
    if best_game is None:
        best_game = game

    # Compare rate of current best game with the element
    if game["Rate"] > best_game["Rate"]:
        best_game = game

print("best_game",best_game)

print("\n\n===== Calculating min value ======")

worst_game = None # Min is unknow yet

for game in games:
    if worst_game is None:
        worst_game = game

    # Compare rate of current worst game with the element
    if game["Rate"] < worst_game["Rate"]:
        worst_game = game

print("worst_game",worst_game)

print("\n\n===== Calculating sum and average value ======")

average = None # Average is unknown yet
rate_sum = None # Sum is unknown yet
number_of_games = len(games)


for game in games:
    if rate_sum is None:
        rate_sum = game["Rate"]
    else: # Only sum from 2nd ward
        # rate_sum = rate_sum + game["Rate"]
        rate_sum += game["Rate"]

print("rate_sum", rate_sum)
# Calculate the average
average = rate_sum / number_of_games
print("average", average)
