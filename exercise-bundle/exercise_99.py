### 99
print("\n===== 99 ======\n")

import json

state = {"level": 5, "items": ["sword"]}

with open("save.txt", "w") as file:
    json.dump(state, file)