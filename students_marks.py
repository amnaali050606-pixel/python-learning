name = input("Enter the name of the student: ")

student_data = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Ayesha": 95,
    "Usman": 88
}

if name in student_data:
    print(f"{name}'s marks are {student_data[name]}")
else:
    print("Student not found")