'''
Grading System
90+ = A
80+ = B
60+ = C
40+ = D
below 40 =F
'''
marks = int(input('Please Enter Your Marks '))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks <90:
    print("Grade B")
elif marks >=60 and marks <80:
    print("Grade C")
elif marks >= 40 and marks <60:
    print("Grade D")
elif marks >= 0 and marks <40:
    print("Grade F")
    print("INVALID")
else:
    print('INVALID INPUT')