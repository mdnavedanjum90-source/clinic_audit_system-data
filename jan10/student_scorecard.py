# Program to calculate the total marks and average marks of a student 

student_name = input("Enter student's name: ").title()
num = int(input("Enter the number of subjects: "))
  
  
total = 0        
          
for i in range(1, num+1):
    marks = int(input(f"Enter the marks of student in subject {i}: "))
    total += marks
    i += 1
    
avg = total / num    
    
if(num==0 or num<0):
    print("Invalid Input")
else:
    print("\n---RESULT SUMMARY---\n")
    print(f"Student's name: {student_name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg}")
