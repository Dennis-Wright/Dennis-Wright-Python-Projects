# Basic Banking System
# Done - Everything!!

import csv

def load_account_info():
    account_list = []

    with open('accounts.csv', 'r') as accounts:
        reader = csv.reader(accounts)

        for account in reader:
            account_list.append(account)
        # End for
    # End with

    return account_list
# End function

def login():
    name = str(input("Enter your name: "))
    account_num = str(input("Enter your account number: "))

    account_attempts = 1

    valid_account, account_index = check_account(name, account_num)

    while valid_account == False:
        if account_attempts < 5:    
            print(f"Error. Invalid name/account number combination. Try again ({account_attempts}/5 attempts)")
            account_attempts += 1           
            print()
            name = str(input("Enter your name: "))
            account_num = str(input("Enter your account number: "))
            valid_account, account_index = check_account(name, account_num)
        else:
            print("Too many attempts. Try again Later")
            raise SystemExit(0)
        # End if
    # End while

    print("Account sucessfully Located.")
    print()
    pin = str(input("Enter your pin number: "))
    pin_correct = check_pin(account_index, pin)

    pin_attempts = 1

    while pin_correct == False:
        if pin_attempts < 3:
            print(f"Error. Incorrect pin. Try again ({pin_attempts}/3 attempts)")
            pin_attempts += 1
            print()
            pin = str(input("Enter your pin number: "))
            pin_correct = check_pin(account_index, pin)
        else:
            print("Too many attempts. Try again Later")
            raise SystemExit(0)
        # End if
    # End while

    print()
    return account_index, name
# End function

# Check if account exists
def check_account(name, num):
    valid_account = False

    counter = 0
    account_index = -1

    for account in account_list:
        if account[0] == name.lower() and account[1] == num:
            valid_account = True
            account_index = counter
            break
        else:
            counter += 1
        # End if
    # End for

    return valid_account, account_index
# End function

# Check if pin correct
def check_pin(account_index, pin):
    correct_pin = False

    if account_list[account_index][2] == pin:
        correct_pin = True
    # End if

    return correct_pin
# End function

def logged_in(account_index, name):
    split_name = name.split(" ") 
    first_name = split_name[0]
    last_name = split_name[1]
    formal_name = first_name[0].upper() + first_name[1::].lower() + " " + last_name[0].upper() + last_name[1::].lower()
    print(f"\nSucessfully Logged In.\n\nWelcome {formal_name}\n\n")
    
    service_decider(account_index)
# End function

def service_decider(account_index):
    print("What service would you like you use? (Enter number)\n1. Deposit\n2. Withdraw\n3. Check Account Balance\n4. Log Out")
    service = int(input("Enter service number: "))

    while service not in [1, 2, 3, 4]:
        print("Error. Incorrect Service Number. Try again\n")
        service = int(input("Enter service number: "))
    # End while
    
    if service == 1:
        Deposit(account_index)
    elif service == 2:
        Withdraw(account_index)
    elif service == 3:
        Balance_Check(account_index)
    elif service == 4:
        Log_Out()
# End function

def get_balance(account_index):
    balance = account_list[account_index][3]
    return int(balance)
# End function

def Deposit(account_index):
    balance = get_balance(account_index)
    print(f"Your current balance is £{balance}")
    amount_to_deposit = int(input("How much would you like to deposit? £"))

    new_balance = balance + amount_to_deposit

    account_list[account_index][3] = new_balance
    
    update_csv()

    print(f"\nDeposit Sucessful!\nYour new balance is £{account_list[account_index][3]}")

    print()
    another = str(input("Would you like to use another service? (y/n) "))

    while another == "y":
        service_decider(account_index)
    else:
        Log_Out()
# End function

def Withdraw(account_index):
    balance = get_balance(account_index)
    print(f"Your current balance is £{balance}")
    amount_to_withdraw = int(input("How much would you like to withdraw? £"))

    while balance - amount_to_withdraw < 0:
        print("Error. Cannot take out more than you have.")
        print()
        amount_to_withdraw = int(input("How much would you like to withdraw? £"))
    # End while

    new_balance = balance - amount_to_withdraw

    account_list[account_index][3] = new_balance

    update_csv()

    print(f"\nWithdrawal Sucessful!\nYour new balance is £{account_list[account_index][3]}")

    print()
    another = str(input("Would you like to use another service? (y/n) "))

    while another == "y":
        service_decider(account_index)
    else:
        Log_Out()
# End function

def Balance_Check(account_index):
    balance = get_balance(account_index)
    print(f"\nYour balance is £{balance}")

    print()
    another = str(input("Would you like to use another service? (y/n) "))

    while another == "y":
        service_decider(account_index)
    else:
        Log_Out()
# End function

def update_csv():
    with open('accounts.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for account in account_list:
            writer.writerow(account)
# End Function

def Log_Out():
    print("\n\nSucessfully Logged Out\n")
    raise SystemExit(0)#
# End function

account_list = load_account_info()
account_index, name = login()
logged_in(account_index, name)