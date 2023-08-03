'''
Pizza Orddering Service
'''
small = 100
medium = 150
large  = 200

#prices for extra cheese in cedis
extra_cheese_s = 10
extra_cheese_m = 20
extra_cheese_l = 30

#prices for extra pepperoni in cedis
extra_pepperoni_s = 15
extra_pepperoni_m = 25
extra_pepperoni_l = 35


menu = '''
   Menu
small = 100
medium = 150
large  = 200
please choose (1) for small, (2) for Medium, and (3) for large! 
'''
extra = '''
extra_cheese
extra_pepperoni
please choose (1) for cheese and (2) for pepperoni! 
'''

user_choise = int(input( menu ))
Quantity1 = int(input('Quantity '))

require_extra = int(input("""Do you want any extra? 
Press (1) for Yes, (2) for No
"""))


if user_choise == 1:
    user_choise1 = small * Quantity1
elif user_choise == 2:
    user_choise1 = medium * Quantity1
elif user_choise == 3:
    user_choise1 = large * Quantity1 
else:
    print("invalid")


if require_extra == 1:
    require_extra1 = int(input(extra))
    Quantity2 = int(input("Quantity"))
    if user_choise == 1 and require_extra1 == 1:
        qty = extra_cheese_s * Quantity2
    elif user_choise == 2 and require_extra1 == 1:
        qty = extra_cheese_m * Quantity2
    elif user_choise == 3 and require_extra1 == 1:
        qty = extra_cheese_l * Quantity2
    elif user_choise == 1 and require_extra1 == 2:
        qty = extra_pepperoni_s * Quantity2
    elif user_choise == 2 and require_extra1 == 2:
        qty = extra_pepperoni_m * Quantity2
    elif user_choise == 3 and require_extra1 == 2:
        qty = extra_cheese_l * Quantity2



if user_choise == 1:
    type = "Small Pizza"
elif user_choise == 2:
    type = "Midium Pizza"
elif user_choise == 3:
    type = "Large Piza"
else:
    type = "Invalid"

print(type)
print(user_choise)
print(user_choise1)
if require_extra ==1:
    total = user_choise1 + qty
    print(qty)
    print(total)
    print( "Total " + str(total)) 


