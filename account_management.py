#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries
# Account Managememt module

import random
import database as db
from database import press_enter_to_continue

def accountExists(accountNumber):
    return (accountNumber in db.accounts)

def createAccount(accountNumber=0,name='',pan='',initialBalance=1000):
    if accountExists(accountNumber):
        db.printerror('EXIST_ERR')
        return
    
    if accountNumber==0:
        identifier=str(random.randint(00000,10000)).ljust(5,'0')
        accountNumber='10000570'+str(identifier)
    # Gathering details (if not already) and appending to db.accounts - dict database
    if (name and pan and initialBalance) == '':
        name=input("Name of the holder: ")
        pan=input("PAN: ")
        initialBalance=float(input("Initial Balance: "))

    # Add the account to dict database
    db.accounts[int(accountNumber)]={
        'name': name, 
        'balance':initialBalance, 
        'pan':pan
    }
    
    print(f"Addition successful. Your account number is {accountNumber}") 
    press_enter_to_continue()
    

def retrieveDetails(accountNumber):
    if not accountExists(accountNumber):
        db.printerror('ABSENT_ERR')
        return
    
    # Gather the name and available balance of account number
    details=db.accounts[accountNumber]

    print(f"Details of the account holder for {accountNumber}:")
    print(f"Name of the Holder: {details['name']} \nBalance: {details['balance']}")