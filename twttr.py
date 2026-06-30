def main():
    text = input("Enter text: ")
    print(remove_vowels(text))

def remove_vowels(text):
    new_text = ""
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    for character in text:
        if character not in vowels:
            new_text += character

    return new_text

main()