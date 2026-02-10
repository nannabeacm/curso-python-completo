### 100
print("\n===== 100 ======\n")

import random
import json

mission_scores = [random.randint(0, 100) for _ in range(10)]

qualified_scores = []
below_avg = []

print("Mission scores: ", mission_scores)

for item in mission_scores:
    if item < 50:
        below_avg.append(item)
    else:
        qualified_scores.append(item)

print("\n===========\n")

print("Qualified: ", qualified_scores)

print("\n===========\n")

average = None
score_sum = 0

for item in mission_scores:
    score_sum += item

average = score_sum / len(mission_scores)

print("Average: ", average)

score_data = {
    "Qualified": qualified_scores,
    "Average": average
}

with open("final_results.txt", "w") as file:
    json.dump(score_data, file)
