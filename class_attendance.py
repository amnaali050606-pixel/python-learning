attendance = {
    "Ali": "Present",
    "Sara": "Absent",
    "Ahmed": "Present",
    "Ayesha": "Present",
    "Usman": "Absent"
}
present_count = 0
absent_count = 0
print("Absent students:")
for student in attendance:
    if attendance[student] == "Absent":
        print(student)
        absent_count += 1
    else:
        present_count += 1
print()
print(f"Present: {present_count}")
print(f"Absent: {absent_count}")