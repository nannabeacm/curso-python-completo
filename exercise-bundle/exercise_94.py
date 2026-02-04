### 94
print("\n===== 94 ======\n")

numbers = [78, 85, 92, 67, 88, 74, 13, 90, 81, 69, 98, 38, 85, 73, 84, 76, 91, 60, 82, 77, 86]

with open("scores.txt", "w") as f:
    for item in numbers:
        f.write(f"{item}\n")

with open("scores.txt", "r") as f:
    lines = f.readlines()

max_score = None
min_score = None
average = None
score_sum = 0
total_of_scores = len(lines)

for line in lines:
    if max_score is None:
        max_score = line
    if line > max_score:
        max_score = line


for line in lines:
    if min_score is None:
        min_score = line
    if line < min_score:
        min_score = line


for line in lines:
    score = int(line)
    score_sum += score


average = score_sum / total_of_scores


all_data = {
    "Maximum score": max_score,
    "Minimum score": min_score,
    "Average score": int(average)
}

with open("report.txt", "w") as f:
    for key, value in all_data.items():
        f.write(f"{key}: {value}\n")
        
