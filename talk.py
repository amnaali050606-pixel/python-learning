import cowsay

animals = ["cow", "dragon", "kitty", "tux", "stegosaurus"]

print("Available animals:")
for animal in animals:
    print("-", animal)

choice = input("Choose an animal: ").lower()
message = input("Message: ")

if choice == "cow":
    cowsay.cow(message)
elif choice == "dragon":
    cowsay.dragon(message)
elif choice == "kitty":
    cowsay.kitty(message)
elif choice == "tux":
    cowsay.tux(message)
elif choice == "stegosaurus":
    cowsay.stegosaurus(message)
else:
    print("Invalid animal")