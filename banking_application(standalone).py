#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries
'''
import csv
import finance_management,account_management
'''

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
    'INPUTERR':'Invalid Input Given',
}
printerror = lambda string: print(f"{string}: {errorDict[string]}")

def enterKeyToContinue():
    input("Press Enter to continue...")
# -------------------------------------------------------------------
# ACCOUNT MANAGEMENT METHODS
# -------------------------------------------------------------------

def checkAccount(accountNumber):
    if accountNumber in accounts:
        return True
    
    return False

def createAccount(accountNumber,name='',initialBalance=1000):
    if checkAccount(accountNumber):
        printerror('EXISTERR')
        #enterKeyToContinue()
        return
    
    # Gathering details and appending to accounts dict database
    if (name and initialBalance) == '':
        name=input("Name of the holder: ")
        initialBalance=float(input("Initial Balance: "))

    # Add the account to dict database
    accounts[accountNumber]={'name': name, 'balance':initialBalance}
    print("Addition successful") if checkAccount(accountNumber) else print("error in adding account")
    #enterKeyToContinue()

def retreiveDetails(accountNumber):
    if not checkAccount(accountNumber):
        printerror('ABSENTERR')
        #enterKeyToContinue()
        return
    
    details=accounts[accountNumber]
    print(f"Details of the account holder for {accountNumber}:")
    print(f"Name of the Holder: {details['name']} \nBalance: {details['balance']}")
    #enterKeyToContinue()
    
# -------------------------------------------------------------------
# METHODS FOR FINANCIAL TRANSACTIONS
# -------------------------------------------------------------------

def validatePAN(pan): 
    if len(pan)==10: return True

def deposit(accountNumber, amount):
    # Constraints
    if not checkAccount(accountNumber):
        printerror('ABSENTERR')
        #enterKeyToContinue()
        return

    if amount>=100000:
        printerror('MAXDEPOSIT')
        pan=input("Enter PAN: ")
        if validatePAN(pan)==False: 
            return
    
    # Deposit - add the amount to balance
    accounts[accountNumber]['balance'] += amount
    print(f"Deposit of {amount} successful")
    #enterKeyToContinue()
    
def withdraw(accountNumber, amount):
    # Constraints
    if not checkAccount(accountNumber):
        printerror('ABSENTERR')
        #enterKeyToContinue()
        return

    balance=accounts[accountNumber]['balance']
    if (amount-balance) < 1000:
        printerror('BALANCEERR')
        #enterKeyToContinue()
        return

    # Withdrawal - remove the amount from balance
    accounts[accountNumber]['balance'] -= amount
    print(f"Withdrawal of {amount} successful")
    #enterKeyToContinue()

def transfer(fromAcc, toAcc, amount=0):
    # Withdraws fromAcc and Deposits toAcc - all constraints followed
    withdraw(fromAcc, amount)
    deposit(toAcc,amount)
    #enterKeyToContinue()

# -------------------------------------------------------------------
# Main Code starts here
# -------------------------------------------------------------------

menu="""
BANKING PORTAL
--ACCOUNT
1] Add a new Account
2] Retreive Account Details
--FINANCE
3] Deposit Amount to Account
4] Withdraw Amount from Account
5] Transfer Amount
Choice: 
"""
while True:
    choice=int(input(menu))
    match choice:
        case 1:
            accountNumber=int(input("Account Number to Add: "))
            createAccount(accountNumber)
            enterKeyToContinue()
        
        case 2:
            accountNumber=int(input("Account Number: "))
            retreiveDetails(accountNumber)
            enterKeyToContinue()

        case 3:
            accountNumber=int(input("Account Number: "))
            amount=float(input("Amount to Deposit: "))
            deposit(accountNumber, amount)
            enterKeyToContinue()

        case 4:
            accountNumber=int(input("Account Number: "))
            amount=float(input("Amount to Withdraw: "))
            withdraw(accountNumber, amount)
            enterKeyToContinue()

        case 5:
            accNum1=int(input("Transfer from: "))
            accNum2=int(input("Transfer to: "))
            amount=int(input("Amount to transfer: "))
            transfer(accNum1,accNum2,amount)
            enterKeyToContinue()
        
        case 0:
            # END
            break
        
        case _:
            printerror('INPUTERR')
            enterKeyToContinue()
        