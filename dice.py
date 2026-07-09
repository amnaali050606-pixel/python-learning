import random

while True:
    roll = input("Roll the dice? (yes/no): ").lower()

    if roll == "yes":
        number = random.randint(1, 6)
        print(f"You rolled: {number}")

    elif roll == "no":
        print("Thanks for playing!")
        break

    else:
        print("Please enter yes or no.")