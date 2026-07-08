expenses = []

while True:
    try:
        num_of_expenses = int(input("How many expenses do you want to enter? "))

        if num_of_expenses <= 0:
            print("Please enter a number greater than 0.")
        else:
            break

    except ValueError:
        print("Please enter a valid integer.")

for i in range(num_of_expenses):
    while True:
        try:
            expense = float(input(f"Enter expense {i + 1}: "))
            expenses.append(expense)
            break
        except ValueError:
            print("Please enter a valid amount.")

total = sum(expenses)
average = total / num_of_expenses
highest_expense = max(expenses)
lowest_expense = min(expenses)

print(f"\nTotal money spent: {total}")
print(f"Average expense: {average:.2f}")
print(f"Highest expense: {highest_expense}")
print(f"Lowest expense: {lowest_expense}")