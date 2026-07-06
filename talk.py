import cowsay

animals = [
    "beavis",
    "cheese",
    "cow",
    "daemon",
    "dragon",
    "fox",
    "ghostbusters",
    "kitty",
    "meow",
    "miki",
    "milk",
    "octopus",
    "pig",
    "stegosaurus",
    "stimpy",
    "trex",
    "turkey",
    "turtle",
    "tux"
]

print("Available animals:")
for animal in animals:
    print("-", animal)

choice = input("\nChoose an animal: ").lower()
message = input("Message: ")

if choice == "beavis":
    cowsay.beavis(message)
elif choice == "cheese":
    cowsay.cheese(message)
elif choice == "cow":
    cowsay.cow(message)
elif choice == "daemon":
    cowsay.daemon(message)
elif choice == "dragon":
    cowsay.dragon(message)
elif choice == "fox":
    cowsay.fox(message)
elif choice == "ghostbusters":
    cowsay.ghostbusters(message)
elif choice == "kitty":
    cowsay.kitty(message)
elif choice == "meow":
    cowsay.meow(message)
elif choice == "miki":
    cowsay.miki(message)
elif choice == "milk":
    cowsay.milk(message)
elif choice == "octopus":
    cowsay.octopus(message)
elif choice == "pig":
    cowsay.pig(message)
elif choice == "stegosaurus":
    cowsay.stegosaurus(message)
elif choice == "stimpy":
    cowsay.stimpy(message)
elif choice == "trex":
    cowsay.trex(message)
elif choice == "turkey":
    cowsay.turkey(message)
elif choice == "turtle":
    cowsay.turtle(message)
elif choice == "tux":
    cowsay.tux(message)
else:
    print("Invalid animal")