questions = {
    "What is the capital of Pakistan?": "Islamabad",
    "How many days are there in a week?": "7",
    "What is 10 + 15?": "25",
    "Which language are you learning?": "Python",
    "What color is the sky on a clear day?": "Blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

print("\nQuiz Finished!")
print(f"Your score is {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.0f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good job!")
else:
    print("Keep practicing!")