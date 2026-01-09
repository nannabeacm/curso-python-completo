# Exercises: Excel & CSV (Stark Industries)

## Mission 1: The Roster (CSV)
Create `roster_maker.py`.
1. Define a dictionary of heroes: name, alias, power_level.
2. Create a Pandas DataFrame.
3. Save it to `heroes.csv`.

## Mission 2: Analysis (CSV)
Create `analyze_roster.py`.
1. Read `heroes.csv` (created in mission 1).
2. Filter for heroes with `power_level > 80`.
3. Print them.

## Mission 3: The Report (Excel)
Create `report_gen.py`.
1. Create a DataFrame with columns: "Month", "Profit".
   - Jan: 1000
   - Feb: 1500
   - Mar: 2000
2. Create a new column "Projected" which is "Profit" * 1.1.
3. Save this to `quarterly_report.xlsx`.

*Note: You need `openpyxl` installed for writing Excel files.*
