print("Marks of student 1 out of 50")
Maths = float(input("Enter marks of Maths :"))
Sci = float(input("Enter marks of Sci:"))
Social = float(input("Enter marks of Social:"))
Eng =  float(input("Enter marks of Eng:"))
Guj = float(input("Enter Guj:"))


marks_list = [Maths, Sci, Social, Eng, Guj]
print(marks_list)

for marks in marks_list:
    if marks <= 10:
       print("You have failed the exam, Better luck next time!")
       exit()       
        
Total = 0
for marks in marks_list:
    Total += marks
print("Total marks", Total)
if Total > 230.0 and Total <= 250.0:
  print("Grade A+")
elif Total > 200.0 and Total <= 230.0:
  print("Grade A")
elif Total > 150.0 and Total <= 200.0:
  print("Grade B+")
elif Total > 100.0 and Total <= 150.0:
  print("Grade B")
elif Total > 50.0 and Total <= 100.0:
  print("Grade C")

