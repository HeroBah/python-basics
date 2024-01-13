# registered_numbers = [
#     {"number": "0541227211", "pin": "1234"},
#     {"number": "0541227212", "pin": "1235"},
#     {"number": "0541227213", "pin": "1236"},
#     {"number": "0541227214", "pin": "1237"},
#     {"number": "0541227215", "pin": "1238"},
#     {"number": "0541227216", "pin": "1239"},
# ]

# you = input('Enter your number: ')

# for m in registered_numbers:
#     if m["number"] == you:
#         pin = input('Enter your PIN: ')
#         if m["pin"] == pin:
#             print("Success")
#         else:
#             print("Incorrect PIN")
#         break
# else:
#     print("Number not registered")

registered_numbers = [
        {"number": "0541227211", "pin": "1234"},
        {"number": "0541227212", "pin": "1235"},
        {"number": "0541227213", "pin": "1236"},
        {"number": "0541227214", "pin": "1237"},
        {"number": "0541227215", "pin": "1238"},
        {"number": "0541227216", "pin": "1239"},
    ]

def check_credentials():
    global registered_numbers
    you = input('Enter your number: ')
    for m in registered_numbers:
        if m["number"] == you:
            pin = input('Enter your PIN: ')
            if m["pin"] == pin:
                print("Success")
            else:
                print("Incorrect PIN")
            return

    print("Number not registered")
    return check_credentials

# Call the function to run the code
check_credentials()