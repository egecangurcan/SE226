studentName = str(input("Enter the Name of the Student:\n"))
studentLabGrade = float(input("Enter the Lab Grade of This Student:\n"))
studentMidtermGrade = float(input("Enter the Midterm Grade of This Student:\n"))
studentFinalGrade = float(input("Enter the Final Grade of This Student:\n"))
lastScore = studentLabGrade * 0.25 + studentMidtermGrade*0.35 + studentFinalGrade*0.4

print("Name: ", studentName)
print("Lab: ", studentLabGrade)
print("Midterm: ", studentMidtermGrade)
print("Final: ", studentFinalGrade)
print("Last Score: ", lastScore)

