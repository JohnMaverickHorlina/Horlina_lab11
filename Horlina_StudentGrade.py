#Student info
name =input("Please enter your name:")
section =input("Please enter your section:")

#Grade 
PrelimGrade = float(input("Enter your PrelimGrade (40-100):"))
if PrelimGrade <40 or PrelimGrade >100:
    print("Invalid input your grade must stay between 40 and 100")
else:
    MidtermGrade = float(input("Enter you MidtermGrade (40-100):"))
if MidtermGrade < 40 or MidtermGrade > 100:
    print ("Invalid input your Grade must be stay between 40 and 100")
else:
    FinalGrade = float(input("Enter your FinalGrade (40-100):"))
if FinalGrade < 40 or FinalGrade >= 100:
    print("Invalid input your grade must stay between 40 and 100")
else:
    PrelimGrade = PrelimGrade * 0.3333
    MidtermGrade = MidtermGrade * 0.3333
    FinalGrade = FinalGrade * 0.3333
    AverageGrade = PrelimGrade + MidtermGrade + FinalGrade
    AverageGrade = round(AverageGrade)

#Greetings
    print()
    print("Hello MR/MS," + name + "!" )
    print("Section"  + section)
    
#GPA
    
if 99 <= AverageGrade <= 100:
    print("a GPA of 1.00 Excellent work!")
elif 96 <= AverageGrade <= 98:  
    print("a GPA of 1.25 Outstanding work!")
elif 93 <= AverageGrade <= 95: 
    print("a GPA of 1.50 Superior work!")
elif 90 <= AverageGrade <= 92: 
    print("a GPA of 1.75 =Very Good work!")
elif 87 <= AverageGrade <= 89: 
    print("a GPA of 2.00 Good Job!")
elif 84 <= AverageGrade <= 86: 
    print("a GPA ofe 2.25 Satisfactory!")
elif 81 <= AverageGrade <= 83: 
    print("a GPA of 2.50 Fairly Satisfactory!")
elif 78 <= AverageGrade <= 80: 
    print("a GPA of 2.75 Fair!")
elif 75 <= AverageGrade <= 77: 
    print("a GPA of 3.00 Passed!")
else:
    print("The grade is below 75 you are failed.Sometimes you may fall short, But a bad grade doesn't define your potential.Keep trying your best life is not a race. ")
    