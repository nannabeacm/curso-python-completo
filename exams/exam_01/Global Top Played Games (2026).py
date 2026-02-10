### EXAM
print("\n===== EXAM ======\n")

import csv

data_file = open("input_game_rates.csv", "r")
file_dict = csv.DictReader(data_file)

game_hours = {}

for line in file_dict:
    game = line["game_title"]
    hours = int(line["hours"])
    if line["date"].startswith("2026-"):
        if game in game_hours:
            game_hours[game] += hours
        else:
            game_hours[game] = hours

sorted_games = sorted(game_hours.items(), key=lambda x: x[1], reverse=True)

top_10_games = sorted_games[:10]

print("Top 10 Most Played Games:")
for i, (game, hours) in enumerate(top_10_games, 1):
    print(f"{i}. {game} - {hours} hours")

with open("top_10_played_games_2026.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["game_title", "total_hours"])
    for game, hours in top_10_games:
        writer.writerow([game, hours])

print("\nTop 10 games written to 'top_10_played_games_2026.csv'")

