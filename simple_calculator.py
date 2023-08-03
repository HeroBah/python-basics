add = "+"
sub = "-"
mult = "*"
divition = "/"
 
user_input_1 = float(input("Enter first digit "))
operator =  input ("Operator ")
user_input_2 =  float(input("Enter secon digit "))

if operator == add:
    result = (user_input_1 + user_input_2)
    print(result)
elif operator == sub:
    result = user_input_1 - user_input_2
    print(result)
elif operator == mult:
    result = user_input_1 * user_input_2
    print(result)
elif operator == divition:
    result = user_input_1 / user_input_2
    print(result)
else:
    result = " Error"

    print(result)