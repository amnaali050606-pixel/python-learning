variable_name = input("enter name of the variable in camel case").replace(" " , "_")
for alphabet in variable_name:
    if alphabet.isupper():
        print("_" , end="")
        print(alphabet.lower() , end="")
    else:
        print(alphabet, end = "")
