# 14. Stark Industries: Automating Excel & CSV

> "I run the business, you protect the world." - Pepper Potts

Business runs on spreadsheets. If you can automate Excel, you are a wizard to them.

**Prerequisites:**
```bash
pip install pandas openpyxl
```

## 1. CSV (Comma Separated Values)
Simple text files pretending to be spreadsheets.

**Reading CSV:**
```python
import pandas as pd

df = pd.read_csv("mission_log.csv")
print(df.head()) # prints first 5 rows
```

**Writing CSV:**
```python
data = {
    "Hero": ["Batman", "Superman"],
    "City": ["Gotham", "Metropolis"]
}

df = pd.DataFrame(data)
df.to_csv("justice_league.csv", index=False)
```

## 2. Excel (`.xlsx`)
The heavy hitter.

**Reading Excel:**
```python
df = pd.read_excel("financials.xlsx", sheet_name="Q1")
```

**Writing Excel:**
```python
df.to_excel("report.xlsx", sheet_name="Summary", index=False)
```

## 3. Automation Logic
Pandas allows you to filter and modify data instantly.

```python
# Filter only Active avengers
active_team = df[df['Status'] == 'Active']

# Calculate total cost
total_cost = df['Cost'].sum()
```

---
**Next Module:** Advanced Powers (Classes & OOP).
