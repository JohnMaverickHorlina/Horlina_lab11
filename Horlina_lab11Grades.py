grades = []
passed_students = []
valid_input = True

while True:
    grade = input("Enter your grade (or type 'nei' to stop ): ")
    
    if grade.lower() == 'nei':
        break
    if not grade.isdigit():
        print("Error : Please enter a numeric grade.")
    else:
        grade = int(grade)
        if grade <= 40 or grade > 100:
            print("Invalid Data")
            valid_input = False
            break
        else:
            grades.append(grade)
            if grade >=  75:
                passed_students.append(grade)
            
if valid_input:
    if grade:
        
        average = sum(grades) / len(grades)
        passing_percentage = (len(passed_students) /len(grades)) * 100
        print(f"Your average grade is:{average:.2f}")
        print(f"Your passing percentage is:{passing_percentage:.2f}%")
        print(f"Your number of students who passed: {len(passed_students)}")
        print(f"Excellent! your grades are: {grades}")
    else:
        print("Y0u dId NoT 3nt3r 7our 6rade")
        
        

