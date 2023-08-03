
#day 1
'''
First_name = "Herobah"
last_name = "Samuel"
Phone_number = int(541227216)
age = int(45)

# how to create a variable

print(Phone_number)
print(age)
print( First_name,last_name )

#how to create a list

names_of_programmes = [ 'Computer Engineering', 'Computer Science', 'Information Technolog',]
second_student =names_of_programmes[1]
print(second_student)


#How to add an element to a list
names_of_programmes.append('Electrical Engineering')
print( names_of_programmes )
'''


# A BMI Calculator
'''BMI Calculator


Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal
Weight is in kg, height is in meters.
Note, that height is a float.'''

#day 2
# names_of_students = ['kofi','Eric', 'Mensah', 'Yeboah', 'HeroBah']
# add_student = names_of_students.append('MK')
# third_student = names_of_students[2]
# remove_last = names_of_students.pop()
# print(names_of_students)
# print(add_student)
# print(remove_last)

#dictionary
# dictionary = {'name': 'Tommy'
#             'age' : '75'
#             'gender' : 'male'
#             'hobies' : {'football', 'bollyball','handball','dancer'}
            
#             }


# students_grades = {'Samuel':'A'
#                  'Kwame':'c'
#                  ' '  
#                 }
 
name = input('Whah is your name? ')
age = input('what is your age? ')
gender = input('what is your gender? ')
#hobies = input('what are your hobbies? ')
print('Hello ', name, 'You are ', age, 'years old')
