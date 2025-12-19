# Basic Login App, Encrypts Password
# Done - Add sign up,Encrypt password, max 3 attempts to login, auto detects if person exists
# To Do - password strength

import csv

def sign_in_or_up():
    print()
    username = str(input("Enter your username (or desired if signing up): "))
    user_exists = False

    with open('logins.csv', 'r') as logins_file:
        reader = csv.reader(logins_file)

        for row in reader:
            if row[0] == username:
                user_exists = True
                user_pswd = row[1]
                break
            # End if
        # End for
    # End with

    if user_exists:
        sign_in(user_pswd)
    else:
        sign_up(username)
    # End if
# End Function

def sign_in(user_pswd):
    password = str(input("Enter your password: "))
    password = encrypt_password(password)

    attempts = 1

    while attempts < 3:
        if user_pswd == password:
            print("Login sucessful!")
            break
        else:
            print(f"Login failed. Try again ({attempts}/3 attempts)")
            attempts += 1
            print()
            password = str(input("Enter your password: "))
            password = encrypt_password(password)
        # End if
    else:
        print("Account locked. Too many attempts.")
    # End While
# End Function

def sign_up(username):
    password = str(input("Enter what you want your password to be (A-Z, a-z, 0-9): "))
    confirm_password = str(input("Enter it again: "))

    while password != confirm_password:
        print("Passwords dont match. Try again.")
        print()
        password = str(input("Enter what you want your password to be (A-Z, a-z, 0-9): "))
        confirm_password = str(input("Enter it again: "))
    # End While

    password = encrypt_password(password)

    with open('logins.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([username, password])
    
    print("Sign-up sucessful. Thank you!")
# End function

def encrypt_password(password):
    letters = {
    # lowercase (reversed)
    "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s",
    "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k",
    "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c",
    "y": "b", "z": "a",

    # digits (reversed)
    "0": "9", "1": "8", "2": "7", "3": "6", "4": "5",
    "5": "4", "6": "3", "7": "2", "8": "1", "9": "0",

    # uppercase (+5 shift)
    "A": "F", "B": "G", "C": "H", "D": "I", "E": "J",
    "F": "K", "G": "L", "H": "M", "I": "N", "J": "O",
    "K": "P", "L": "Q", "M": "R", "N": "S", "O": "T",
    "P": "U", "Q": "V", "R": "W", "S": "X", "T": "Y",
    "U": "Z", "V": "A", "W": "B", "X": "C", "Y": "D",
    "Z": "E"
    }

    encrypted_password = ""

    for letter in password:
        encrypted_password = encrypted_password + letters[letter]
    # End for

    return encrypted_password
# End function


sign_in_or_up()