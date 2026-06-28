fruits = ["apple", "banana", "mango", "orange"]
print("Original list:", fruits)
fruits.append("grapes")
print("After adding grapes:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)
print("First fruit:", fruits[0])
print("Total fruits:", len(fruits))
print("Fruit names:")
for fruit in fruits:
    print(fruit)