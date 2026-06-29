subject = input(" enter the name of the subject").lower()
subjects_grades = {
    "math" :"A" ,
    "english" : "B+" ,
    "physics" :"A-" ,
    "chemistry" :"B" ,
    "biology" :"A" , 
    "computer science" :"A+" ,
    "history" :"C+" ,
    "urdu" :"B"
}
if subject in subjects_grades:
    print(subjects_grades[subject])
else:
    print ("subject not found")
