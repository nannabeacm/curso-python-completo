### EXAM
print("\n===== EXAM ======\n")

import csv

with open("input_game_rates.csv", "r") as data_file:
    file_reader = csv.DictReader(data_file)
    all_data = list(file_reader)

def user_top_3(target_username):
    game_hours = {}
    
    for line in all_data:
        game = line["game_title"]
        hours = int(line["hours"])
        username = line["username"]
        date = line["date"]
        
        if username == target_username and date.startswith("2026-"):
            if game in game_hours:
                game_hours[game] += hours
            else:
                game_hours[game] = hours

    sorted_games = sorted(game_hours.items(), key=lambda x: x[1], reverse=True)

    top_3_games = sorted_games[:3]
    
    print(f"Top 3 Most Played Games for {target_username}:")
    for i, (game, hours) in enumerate(top_3_games, 1):
        print(f"{i}. {game} - {hours} hours")

    output_filename = f"{target_username}_top_3_games.csv"
    with open(output_filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["game_title", "total_hours"])
        for game, hours in top_3_games:
            writer.writerow([game, hours])

    print(f"\nTop 3 games of {target_username} written to : {output_filename}")


user_top_3("User_01")
user_top_3("User_02")
user_top_3("User_03")
user_top_3("User_04")
user_top_3("User_05")
user_top_3("User_06")
user_top_3("User_07")
user_top_3("User_08")
user_top_3("User_09")
user_top_3("User_10")