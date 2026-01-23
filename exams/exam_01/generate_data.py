
import csv
import random
from datetime import datetime, timedelta

# Configuration
NUM_ROWS = 1000
NUM_USERS = 10
NUM_GAMES = 20
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 12, 31)

# lists
USERS = [f"User_{i:02d}" for i in range(1, NUM_USERS + 1)]
GAMES = [
    "The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey", "Red Dead Redemption 2", "The Witcher 3: Wild Hunt",
    "God of War", "Elden Ring", "Minecraft", "Fortnite", "Overwatch 2", "Call of Duty: Modern Warfare II",
    "Cyberpunk 2077", "Hades", "Stardew Valley", "Animal Crossing: New Horizons", "Hollow Knight",
    "Celeste", "Dark Souls III", "Bloodborne", "Sekiro: Shadows Die Twice", "Baldur's Gate 3"
]

def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

def generate_data():
    data = []
    # Header
    header = ["username", "game_title", "rate", "date", "hours", "played"]
    
    for _ in range(NUM_ROWS):
        username = random.choice(USERS)
        game_title = random.choice(GAMES)
        rate = random.randint(1, 5)
        date = random_date(START_DATE, END_DATE).strftime("%Y-%m-%d")
        hours = random.randint(1, 100) # Random hours played in a session/entry
        played = "Yes" # Assuming played is a boolean-like or status, using "Yes" for simplicity based on description "played"
        # Re-reading prompt: "hours,played". Could be hours_played as one column or two. 
        # "username,game_title,rate(1-5),date,hours,played" -> 6 columns.
        # Let's assume 'played' is maybe total hours? Or just a flag? 
        # The prompt says "hours,played" as the last part. 
        # Let's look closer: "username,game_title,rate(1-5),date,hours,played"
        # It asks for "hours, played".
        # Maybe it meant "hours_played"? 
        # "The student needs to create a program that process a file containing game rates from 15 users. The file should be a csv and contain username,game_title,rate(1-5),date,hours,played"
        # I will treat "hours" as hours played in that session and "played" as a status or maybe a typo for "hours_played" being one column? 
        # PROMPT: "username,game_title,rate(1-5),date,hours,played" -> 6 items. 
        # I will assume 'played' is a boolean 'True' or '1' indicicating completion or just '1' for record.
        # Actually, let's assume 'played' follows 'hours' and might mean something else. 
        # Let's stick to the column names exactly: username, game_title, rate, date, hours, played.
        # I'll put 'played' as 'True' for now.
        
        row = [username, game_title, rate, date, hours, "True"]
        data.append(row)
        
    return header, data

def write_csv(filename, header, data):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == "__main__":
    header, data = generate_data()
    output_path = "exams/exam_01/input_game_rates.csv"
    write_csv(output_path, header, data)
    print(f"Generated {NUM_ROWS} rows to {output_path}")
