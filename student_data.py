student_data = {} 
while True:
    try:
         student_name = input("enter the name of student")
         if student_name.lower() == "done":
          break
         marks = int(input("enter marks of the studnent"))
         student_data[student_name] = marks 
         
    except ValueError:
       print(" enter a numeric value")

for student , marks in student_data.items():
           print(f"Student: {student}, Marks: {marks}")   
if len(student_data) == 0:
    print("No student data entered.")
else:
 highest_marks = 0 
 top_student = ""
 for student , marks in student_data.items():
   if highest_marks < marks :
      highest_marks = marks 
      top_student= student
print (f" student name:{top_student} , heighest_marks: {highest_marks}")