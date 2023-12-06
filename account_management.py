#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries
# Account Managememt module

import database as db

def accountExists(accountNumber):
    return (accountNumber in db.accounts)

def createAccount(accountNumber,name='',pan='',initialBalance=1000):
    if accountExists(accountNumber):
        db.printerror('EXIST_ERR')
        return
    
    # Gathering details (if not already) and appending to db.accounts - dict database
    if (name and pan and initialBalance) == '':
        name=input("Name of the holder: ")
        pan=input("PAN: ")
        initialBalance=float(input("Initial Balance: "))

    # Add the account to dict database
    db.accounts[accountNumber]={
        'name': name, 
        'balance':initialBalance, 
        'pan':pan
    }
    
    print("Addition successful") if accountExists(accountNumber) else print("error in adding account")
    

def retreiveDetails(accountNumber):
    if not accountExists(accountNumber):
        db.printerror('ABSENT_ERR')
        return
    
    # Gather the name and available balance of account number
    details=db.accounts[accountNumber]

    print(f"Details of the account holder for {accountNumber}:")
    print(f"Name of the Holder: {details['name']} \nBalance: {details['balance']}")