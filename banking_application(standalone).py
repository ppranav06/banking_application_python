#!/usr/bin/env python3

# Banking application using python - implemented via dictionaries

accounts={
    # Format: 10000|570|00000 - Bank|Branch|AccountNumber
    1000057000000:{
        'name':str(),
        'balance':float()
    }
}

errorDict={
    'INVALID_ERR':'Invalid Account Number',
    'ABSENT_ERR':'Account not found',
    'EXIST_ERR':'Account already exists',
    'INSUF_FUNDS_ERR':'Insufficient Balance',
    'MIN_BALANCE_ERR':'Minimum Balance not maintained',
    'MAXLIMIT_ERR':'Maximum Deposit Limit is 100000',
    'INPUT_ERR':'Invalid Input Given',
}
printerror = lambda string: print(f"{string}: {errorDict[string]}")

def press_enter_to_continue():
    input("Press Enter to continue...")
def account_number_validity(accountNumber):
    return (len(str(accountNumber))==13) and ('10000570' in str(accountNumber))


# -------------------------------------------------------------------
# ACCOUNT MANAGEMENT METHODS
# -------------------------------------------------------------------

def accountExists(accountNumber):
    if accountNumber in accounts:
        return True
    
    return False

def createAccount(accountNumber,name='',initialBalance=1000):
    if accountExists(accountNumber):
        printerror('EXIST_ERR')
        return
    
    # Gathering details and appending to accounts dict database
    if (name and initialBalance) == '':
        name=input("Name of the holder: ")
        initialBalance=float(input("Initial Balance: "))

    # Add the account to dict database
    accounts[accountNumber]={'name': name, 'balance':initialBalance}
    print("Addition successful") if accountExists(accountNumber) else print("error in adding account")
    

def retreiveDetails(accountNumber):
    if not accountExists(accountNumber):
        printerror('ABSENT_ERR')
        return
    
    # Gather the name and available balance of account number
    details=accounts[accountNumber]
    print(f"Details of the account holder for {accountNumber}:")
    print(f"Name of the Holder: {details['name']} \nBalance: {details['balance']}")
    
    
# -------------------------------------------------------------------
# METHODS FOR FINANCIAL TRANSACTIONS
# -------------------------------------------------------------------

def validatePAN(pan): 
    return len(pan) == 10 and pan.isalnum()

def deposit(accountNumber, amount):
    # Constraints
    if not accountExists(accountNumber):
        printerror('ABSENT_ERR')
        return

    if amount>=100000:
        printerror('MAXDEPOSIT')
        pan=input("Enter PAN: ")
        if validatePAN(pan)==False: 
            return
    
    # Deposit - add the amount to balance
    accounts[accountNumber]['balance'] += amount
    print(f"Deposit of {amount} successful")
    
def withdraw(accountNumber, amount):
    # Constraints
    if not accountExists(accountNumber):
        printerror('ABSENT_ERR')
        return

    existing=accounts[accountNumber]['balance']
    
    # withdraw past available money prevention - insufficient funds
    if amount > existing:
        printerror('INSUF_FUNDS_ERR')
        print("Transaction Failed")
        return

    # withdraw prevention if balance < 1000
    if (amount-existing) < 1000:
        printerror('MIN_BALANCE_ERR')
        print("Transaction Failed")
        return

    # Withdrawal - remove the amount from balance
    accounts[accountNumber]['balance'] -= amount
    print(f"Withdrawal of {amount} successful")
    

def transfer(fromAcc, toAcc, amount):
    # Withdraws fromAcc and Deposits toAcc - all constraints followed

    if fromAcc not in accounts or toAcc not in accounts:
        printerror('ABSENT_ERR')
        print("Atleast one of the account numbers doesn't exist.")
        return
    
    if (amount - accounts[fromAcc]['balance']) < 1000:
        printerror('BALANCE_ERR')
        return
    
    if (amount + accounts[toAcc]['balance']) >= 100000:
        printerror('MAXLIMIT_ERR')
        pan=input("Enter PAN: ")
        if validatePAN(pan)==False: 
            printerror('PAN_ERR')
            return

    accounts[fromAcc]['balance'] -= amount  #withdraw(fromAcc, amount)
    accounts[toAcc]['balance'] += amount    #deposit(toAcc,amount)
    print(f"Transfer of {amount} from {fromAcc} to {toAcc} successful.")

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
    # the 
    if not accountExists(accountNumber):
        printerror('ABSENT_ERR')
        continue
    if not account_number_validity(accountNumber):
        printerror('INVALID_ERR')
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
        