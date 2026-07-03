colors = {}

while True:
    color = input("Enter your favorite color: ").lower()

    if color == "done":
        break

    if color in colors:
        colors[color] += 1
    else:
        colors[color] = 1

print("\nColor Count:")

for color in sorted(colors):
    print(f"{color}: {colors[color]}")