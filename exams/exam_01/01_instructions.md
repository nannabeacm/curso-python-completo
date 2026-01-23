# Exam 01: Game Rates Processing

## Objective
Create a program that processes a file containing game rates from users and generates specific reports.

## Input
You will be provided with a CSV file named `input_game_rates.csv`.
The file contains data for 10 users and 20 game titles over the period of 2024-2026.

### File Format:
- **Type**: CSV
- **Columns**: `username`, `game_title`, `rate`, `date`, `hours`, `played`
- **Rate**: 1-5 scale

## Requirements

### Process
Your program must read the input file and process the data to generate the following outputs.

### Outputs

#### 1. Global Top Played Games (2026)
- **Filename**: `top_10_played_games_2026.csv`
- **Content**: A list of the top 10 played games in the year 2026 based on the data.
- **Criteria**: Ranking should be based on the number of entries or total hours played (interpret "played" relevance as needed, usually total engagement).

#### 2. User Specific Reports
- **Filename Pattern**: `[username]_top_3_games.csv` (e.g., `User_01_top_3_games.csv`)
- **Quantity**: Up to 15 files (one for each unique user found in the input, which is 10 in the provided sample but code should handle up to 15).
- **Content**: The top 3 games played by that specific user.
- **Criteria**: Ranking based on highest rating given, or most hours played if ratings are tied.

## Detailed Instructions
1. Load the `input_game_rates.csv` file.
2. Filter data for the year 2026 to calculate the global top 10.
3. Group data by user to generate individual reports.
4. Ensure your code is clean, well-commented, and handles the CSV format correctly.
