def check_password(password):
    length = len(password)
    has_digit = False
    has_upper = False
    has_lower = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True

    if length >= 8 and has_digit and has_upper and has_lower:
        return "Strong password"
    elif length >= 6:
        return "Medium password"
    else:
        return "Weak password"


password = input("Enter your password: ")

result = check_password(password)

print(result)