#!/usr/bin/env python3
# DATABASE
# This is the database for all accounts, PANs and Error messages. 
# Every speck of data and the function to validate if the data 
# follows the format comes from here.

# All account numbers - database
accounts={
    # Format: 10000|570|00000 - Bank|Branch|AccountNumber
    1000057000000:{
        'name':str(),
        'pan':str(),
        'balance':float()
    }
}

def account_number_validity(accountNumber):
    # Format: 10000|570|00000 - Bank|Branch|AccountNumber
    accountNumber=str(accountNumber)
    return (len(accountNumber)==13) and ('10000570' in accountNumber)

# PAN database - to verify for huge transfers

PAN={
    'AQIPX4421P':
    {'name': 'John Doe',
     'dob':'1996/12/25'},

    'AMXCR9873B':
    {'name': 'Alice Bob',
     'dob': '1983/5/22'},

    'LMSTB2154O':
    {'name': 'Spongebob Squarepants',
     'dob': '1977/2/16'},
}


def validatePAN(pan, accountNumber): 
    if (len(pan)!=10) or (pan[3] not in ('P','T','C')):
        printerror('INVALID_PAN_ERR')
        return
    
    return 'matching' if (pan == accounts[accountNumber]['pan']) else 'not matching'


# Possible errors and their error messages

errorDict={
    'INVALID_ERR':'Invalid Account Number',
    'ABSENT_ERR':'Account not found',
    'EXIST_ERR':'Account already exists',

    'INVALID_PAN_ERR':'Invalid PAN entered',
    
    'INSUF_FUNDS_ERR':'Insufficient Balance',
    'MIN_BALANCE_ERR':'Minimum Balance not maintained',
    'MAXLIMIT_ERR':'Maximum Deposit Limit is 100000',
    
    'INPUT_ERR':'Invalid Input Given',
}

def printerror (errorIdentifier): 
    print(f"{errorIdentifier}: {errorDict[errorIdentifier]}")
    press_enter_to_continue()

def press_enter_to_continue():
    input("Press Enter to continue...")

