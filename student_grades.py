student_data = {}

while True:
    name = input("Enter the student's name: ")

    if name.lower() == "done":
        break

    while True:
        grade = input("Enter the student's grade (A, B, C, D, F): ").upper()

        if grade in ["A", "B", "C", "D", "F"]:
            break
        else:
            print("Invalid grade! Please enter A, B, C, D, or F.")

    student_data[name] = grade

print("\nStudent Grades:")
for name, grade in student_data.items():
    print(f"{name}: {grade}")

grade_count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

for grade in student_data.values():
    grade_count[grade] += 1

print("\nGrade Summary:")
for grade, count in grade_count.items():
    print(f"{grade}: {count}")