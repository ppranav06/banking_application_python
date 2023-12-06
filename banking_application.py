#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries

import string
import os

# Essentials
from account_management import *
from finance_management import *
from database import *

# -------------------------------------------------------------------
# Main Code starts here
# -------------------------------------------------------------------

def cls():
    os.system('cls') if os.name=='nt' else os.system('clear')

menu="""
BANKING PORTAL
--FINANCE
1] Withdraw Amount from Account
2] Deposit Amount to Account
3] Transfer Amount
--ACCOUNT
4] Retreive Account Details
Choice: (0 to logout)
"""
while True:
    cls()
    print("XYZ BANK LIMITED \nBANKING PORTAL")
    print("(Enter 0 to exit)")

    accountNumber=int(input("Account Number: "))

    # the validity is checked before account number
    if not account_number_validity(accountNumber):
        printerror('INVALID_ERR')
        createAccount(00000) if input("Would you like to create an account? (y/n)") in ('y', 'Y') else None
        continue

    # if account does not exist, create a new one
    if not accountExists(accountNumber):
        printerror('ABSENT_ERR')
        createAccount(00000) if input("Would you like to create an account? (y/n)") in ('y', 'Y') else None
        continue
    
    # USER MENU
    while True:
        choice = int(input(menu))
        
        if choice == 1:
            amount = float(input("Amount to Withdraw: "))
            withdraw(accountNumber, amount)
            press_enter_to_continue()

        elif choice == 2:
            amount = float(input("Amount to Deposit: "))
            deposit(accountNumber, amount)
            press_enter_to_continue()

        elif choice == 3:
            accNum2 = int(input("Transfer to: "))
            amount = int(input("Amount to transfer: "))
            transfer(accountNumber, accNum2, amount)
            press_enter_to_continue()

        elif choice == 4:
            retrieveDetails(accountNumber)
            press_enter_to_continue()

        elif choice == 0:
            # END
            cls()
            break
        
        else:
            printerror('INPUT_ERR')
            press_enter_to_continue()

    if accountNumber==0:
        # END
        print("Exiting.")
        break

    