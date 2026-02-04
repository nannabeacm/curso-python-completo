### 97
print("\n===== 97 ======\n")

super_quiz = {
    "When was Quicksilver created?": "1964",
    "Is Quicksilver a X-Men or an Avenger?": "Avenger",
    "What's Quicksilver's full name?": "Pietro Django Maximoff",
    "What's Quicksilver's daughter's name?": "Luna Maximoff",
    "Is Quicksilver a mutant?": "No",
    "What's Quicksilver's super-power?": "Super-speed"
}

print("Welcome to the SUPER-QUIZ.")

score = 0

def ask_user(question, right_answer, score):
    user_answer = input(question + "\n")
    if user_answer.lower() == right_answer.lower():
        score += 1
        print("Correct!")
        print("Score: ", score)
    else:
        print("Wrong! Right answer: ", right_answer)
        print("Score: ", score)
    return score

for question, correct_answer in super_quiz.items():
    score = ask_user(question, correct_answer, score)

if score == 6:
    print("Well done! You got everything right!")
elif score == 0:
    print("At least you tried, right?")
else:
    print("Good run! You should try again! ", score, " out of 6 right!")