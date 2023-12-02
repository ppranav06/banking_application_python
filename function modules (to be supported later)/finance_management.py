#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries
# Financial transactions module

import csv
from account_management import *

errorDict={
    'INVALIDERR':'Invalid Account Number',
    'ABSENTERR':'Account not found',
    'EXISTERR':'Account already exists',
    'BALANCEERR':'Insufficient Balance',
    'MAXDEPOSIT':'Maximum Deposit Limit is 100000',
    'PANERR':'Inavlid PAN (Permanent Account Number)',
}
printerror = lambda string: print(errorDict[string])

def validatePAN(pan): 
    if len(pan)==10: return True

def deposit(accountNumber, amount):
    # Constraints
    if not checkAccount(accountNumber):
        printerror('ABSENTERR')
        return

    if amount>=100000:
        printerror('MAXDEPOSIT')
        pan=input("Enter PAN: ")
        if validatePAN(pan)==False: 
            return
    
    # Deposit - add the amount to balance
    accounts[accountNumber]['balance'] += amount
    
def withdraw(accountNumber, amount):
    # Constraints
    if not checkAccount(accountNumber):
        printerror('ABSENTERR')
        return

    balance=accounts[accountNumber]['balance']
    if (amount-balance) < 1000:
        printerror('BALANCEERR')
        return

    # Withdrawal - remove the amount from balance
    accounts[accountNumber]['balance'] -= amount

def transfer(fromAcc, toAcc, amount):
    # Withdraws fromAcc and Deposits toAcc - all constraints followed
    withdraw(fromAcc, amount)
    deposit(toAcc,amount)
