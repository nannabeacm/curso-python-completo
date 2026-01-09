# Exercises: requests (Cerebro)

## Mission 1: Who's that Pokemon?
Create `pokedex.py`.
1. Ask the user for a Pokemon name.
2. Use `requests` to get data from `https://pokeapi.co/api/v2/pokemon/{name}`.
3. If `status_code` is 200:
   - Print its Name, ID, and Types.
4. If `status_code` is 404:
   - Print "Pokemon not found in database."

## Mission 2: Space Station Tracker
Create `iss.py`.
The API `http://api.open-notify.org/iss-now.json` tells you where the International Space Station is.
1. Fetch the data.
2. Print the Latitude and Longitude.
3. (Bonus) Run this in a loop every 5 seconds (use `time.sleep(5)`) to track it live.

## Mission 3: Joke Generator
Create `joker.py`.
Find a free joke API (like `https://official-joke-api.appspot.com/random_joke`).
Fetch a joke.
Print the "setup".
Wait 2 seconds (time.sleep).
Print the "punchline".
