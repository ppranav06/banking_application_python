#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries
# Account Managememt module

import csv

accounts={
    0000000000000:{
        'name':str(),
        'balance':float()
    }
}

errorDict={
    'INVALIDERR':'Invalid Account Number',
    'ABSENTERR':'Account not found',
    'EXISTERR':'Account already exists',
    'BALANCEERR':'Insufficient Balance',
    'MAXDEPOSIT':'Maximum Deposit Limit is 100000',
    'PANERR':'Inavlid PAN (Permanent Account Number)',
}
printerror = lambda string: print(errorDict[string])


def checkAccount(accountNumber):
    if accountNumber in accounts.keys():
        return True
    
    return False

def createAccount(accountNumber,name,initialBalance):
    if checkAccount(accountNumber)==True:
        print(f"E2: Account Number {accountNumber} already exists. Enter a new number.")
        return

    accountDetails={'name': name, 'balance':initialBalance}

    accounts[accountNumber]=accountDetails

def retreiveDetails(accountNumber):
    if checkAccount(accountNumber)==False:
        print("E1: Account Number not found.")
        return
    
    details=accounts[accountNumber]
    print(f"Account Number: {accountNumber} \nName of the Holder: {details['name']} \nBalance: {details['balance']}")
    
