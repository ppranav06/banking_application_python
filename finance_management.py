#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries
# Financial transactions module

from account_management import *
import database as db

def deposit(accountNumber, amount):
    # Constraints
    if not accountExists(accountNumber):
        db.printerror('ABSENT_ERR')
        return

    if amount>=100000:
        db.printerror('MAXDEPOSIT')
        pan=input("Enter PAN: ")
        if db.validatePAN(pan)==False: 
            return
    
    # Deposit - add the amount to balance
    db.accounts[accountNumber]['balance'] += amount
    print(f"Deposit of {amount} successful")


def withdraw(accountNumber, amount):
    # Constraints
    if not accountExists(accountNumber):
        db.printerror('ABSENT_ERR')
        return

    existing=db.accounts[accountNumber]['balance']
    
    # withdraw past available money prevention - insufficient funds
    if amount > existing:
        db.printerror('INSUF_FUNDS_ERR')
        print("Transaction Failed")
        return

    # withdraw prevention if balance < 1000
    if (amount - existing) < 1000:
        db.printerror('MIN_BALANCE_ERR')
        print("Transaction Failed")
        return

    # Withdrawal - remove the amount from balance
    db.accounts[accountNumber]['balance'] -= amount
    print(f"Withdrawal of {amount} successful")
    

def transfer(fromAcc, toAcc, amount):
    # Withdraws fromAcc and Deposits toAcc - all constraints followed

    if (fromAcc not in db.accounts) or (toAcc not in db.accounts):
        db.printerror('ABSENT_ERR')
        print("At least one of the account numbers doesn't exist.")
        return
    
    balance_fromAcc=db.accounts[fromAcc]['balance']
    balance_toAcc=db.accounts[toAcc]['balance']

    if amount > balance_fromAcc: 
        db.printerror('INSUF_FUNDS_ERR')
        return

    if (amount - balance_fromAcc) < 1000:
        db.printerror('BALANCE_ERR')
        return

    totalFunds=balance_toAcc+amount
    if (totalFunds >= 100000):  
        db.printerror('MAXLIMIT_ERR')
        pan=input("Enter PAN: ")
        if db.validatePAN(pan,toAcc)=='not matching': 
            db.printerror('PAN_ERR')
            print("Transaction Failed")
            return

    db.accounts[fromAcc]['balance'] -= amount  #withdraw(fromAcc, amount)
    db.accounts[toAcc]['balance'] += amount    #deposit(toAcc,amount)
    print(f"Transfer of {amount} from {fromAcc} to {toAcc} successful.")