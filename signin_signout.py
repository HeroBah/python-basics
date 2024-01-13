users = [
    {"username": "sammy", "password": "1234", "status": "active"}
    {"username": "santos", "password": "1235", "status": "active"}

]

username = input("enter user name ")
password = input("enter password ")

def sign_in ():
    global username
    global password
    global users
    for m in users:
        