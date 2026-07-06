import random

best_score = None

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low!")

            elif guess > secret_number:
                print("Too high!")

            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("New best score!")

                print(f"Best score: {best_score} attempts")
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break