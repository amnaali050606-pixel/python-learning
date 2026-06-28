def main():
    text  = input(" enter text ")
    new_text = ""
    remove_vowels(text)
    character = [ "a" , "A" , "e" , "E" , "i" , "I" , "o" , "O" ,"u" , "U"]
def remove_vowels(text):
    for character in text :
        if text == character :
         new_text = text.remove(character)
        else:
            print()
        return new_text

main()