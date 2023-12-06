#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries

import string
import os

from account_management import *
from finance_management import *
from database import *

# -------------------------------------------------------------------
# Main Code starts here
# -------------------------------------------------------------------

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
    accountNumber=int(input("Account Number: "))
    # the validity is checked before account number
    if not account_number_validity(accountNumber):
        printerror('INVALID_ERR')
        continue
    if not accountExists(accountNumber):
        printerror('ABSENT_ERR')
        continue
    
# FUNCTIONALITY TO ADD:
# CREATE AN ACCOUNT FROM MENU SOMEHOW
    choice=int(input(menu))
    # switch-case statement to implement menu-driven portal
    match choice:
        case 1:
            amount=float(input("Amount to Withdraw: "))
            withdraw(accountNumber, amount)
            press_enter_to_continue()

        case 2:
            amount=float(input("Amount to Deposit: "))
            deposit(accountNumber, amount)
            press_enter_to_continue()

        case 3:
            accNum2=int(input("Transfer to: "))
            amount=int(input("Amount to transfer: "))
            transfer(accountNumber,accNum2,amount)
            press_enter_to_continue()

        case 4:
            retreiveDetails(accountNumber)
            press_enter_to_continue()
     
        case 0:
            # END 
            break
        
        case _:
            printerror('INPUT_ERR')
            press_enter_to_continue()
        