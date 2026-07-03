fruits = {}

while True:
    name = input("Enter the name of a fruit: ").lower()

    if name == "done":
        break

    if name in fruits:
        fruits[name] += 1
    else:
        fruits[name] = 1

print("\nFruit Count:")

for fruit in sorted(fruits):
    print(f"{fruit}: {fruits[fruit]}")