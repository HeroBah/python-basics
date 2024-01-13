# import list_dictionary
# enter_mobile_number = list_dictionary.check_credentials()
code = input()

menu ='''   Menu
1. Transfer Muney
2. MoMoPay & Pay Bill
3. Airtime
4. Allow Cash Out
5. Finatial Services
6. My Walet
7. MoMo Promo
'''

def transfer_money():
    import list_dictionary  
    transfer_money = input('''
Transfer Money
1. MoMo User
2. Non MoMo User
3. Send With Care
4. Favorate
5. Other Networks
6. Bank Account
0. Back

                           
''')
    mobile_num = list_dictionary.check_credentials()
    return(transfer_money)
    
    
# ----------->  transfer_money Ends here  <-----------------------

# -------------------> *170# code starts here <---------

if code == "*170#":
    menu = (int(input(menu)))
else:
    print("Invalid Code")
 # -------------------> *170# code ends here <---------

if menu == 1:
    print(transfer_money())
else:
    print( "Invalid Input" )
