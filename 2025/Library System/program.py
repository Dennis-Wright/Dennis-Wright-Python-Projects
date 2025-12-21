import csv, string

def load_files():

    books = []
    borrowed = []

    with open('books.csv', 'r') as books_data:
        reader = csv.reader(books_data)

        for book in reader:
            books.append(book)
        # End for
    # End With

    with open('borrowed.csv', 'r') as borrowed_data:
        reader = csv.reader(borrowed_data)

        for data in reader:
            borrowed.append(data)
        # End for
    # End with

    return books, borrowed
# End Function

# Lines 29 - 138 is for the sign in/up system

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
        current_user = sign_in(user_pswd, username)
    else:
        current_user = sign_up(username)

    return current_user
    # End if
# End Function

def sign_in(user_pswd, username):
    password = str(input("Enter your password: "))
    password = encrypt_password(password)

    current_user = username

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
        raise SystemExit(0)

    return current_user
    # End While
# End Function

def sign_up(username):
    password = str(input("Enter what you want your password to be (A-Z, a-z, 0-9): "))

    allowed = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    while not all(char in allowed for char in password):
        print("Error - password can only contain letters and numbers.")
        password = str(input("Enter what you want your password to be (A-Z, a-z, 0-9): "))
    # End while

    confirm_password = str(input("Enter it again: "))

    while password != confirm_password:
        print("Passwords dont match. Try again.")
        print()
        password = str(input("Enter what you want your password to be (A-Z, a-z, 0-9): "))

        while not all(char in allowed for char in password):
            print("Error - password can only contain letters and numbers.")
            password = str(input("Enter what you want your password to be (A-Z, a-z, 0-9): "))
        # End while

        confirm_password = str(input("Enter it again: "))
    # End While

    password = encrypt_password(password)

    with open('logins.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([username, password])
    
    print("Sign-up sucessful. Thank you!\n")
    current_user = username
    return current_user
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

# Lines 141 and below is for the library system

def service_decider(books, borrowed, current_user):
    print("\nWhat would you like to do today?\n1. View All Books\n2. Search for a book (by title and author)\n3. Borrow a book\n4. Return a book\n5. Show all books borrowed by a user\n6. Exit")
    service = int(input("Enter the number for the service you would like to use: "))

    while service not in [1, 2, 3, 4, 5, 6]:
        print("\nInvalid Service Number. Try Again.")
        service = int(input("Enter the number for the service you would like to use: "))
    # End while

    
    if service == 1:
        view_all(books)
    elif service == 2:
        search(books)
    elif service == 3:
        borrow(books, borrowed, current_user)
    elif service == 4:
        return_book(books, borrowed, current_user)
    elif service == 5:
        show_all_by_user(books, borrowed, current_user)
    elif service == 6:
        Log_Out(books, borrowed)  
# End function

def view_all(books):
    print("\n----- ALL BOOKS -----")
    for book in books:
        print(f"{book[1]} by {book[2]}. Avaliable - {book[3]}")
    # End for

    return
    # End if
# End function

def search(books):
    print()
    book_to_search_for = str(input("Enter the title of a book to search for: ")).lower()
    author_of_book = str(input("Enter the name of the author of that book: ")).lower()

    found = False

    for book in books:
        if book[1].lower() == book_to_search_for and book[2].lower() == author_of_book:
            if book[3] == "Yes":
                avaliable = "avaliable to borrow"
            else:
                avaliable = "mot avaliable to borrow"
            # End If

            print(f"\n{book[1]} by {book[2]} is in our collection. It is currently {avaliable}")
            found = True
            break
        # End if
    # End for

    if found == False:
        print(f"\nWe do not have {book_to_search_for} by {author_of_book} in our collection.")
    # End if

    return
    # End if
# End function
        
def borrow(books, borrowed, current_user):
    book_to_borrow = str(input("\nWhat book would you like to borrow: ")).lower()
    author_of_book = str(input("What is the author's name: ")).lower()

    for book in books:
        if book_to_borrow == book[1].lower() and author_of_book == book[2].lower():
            if book[3] == "Yes":
                borrow_or_not = str(input(f"\n{book[1]} by {book[2]} is avaliable to borrow. Would you like to borrow it? (y/n) ")).lower()

                if borrow_or_not == "y":
                    book[3] = "No"
                    borrowed.append([current_user, book[1]])
                    print(f"You have borrowed {book[1]} by {book[2]}")
                    return
                elif borrow_or_not == "n":
                    print(f"No worries.")
                    return
                # End if
            elif book[3] == "No":
                print(f"\n{book[1]} by {book[2]} is not avaliable to borrow.")
                return
            # End if
        # End if
    # End for
# End function

def return_book(books, borrowed, current_user):
    book_to_return = str(input("\nWhat book would you like to return: ")).lower()

    for entry in borrowed:
        if entry[0] == current_user and entry[1].lower() == book_to_return:
            print("\nBook returned\n")
            borrowed.remove(entry)
            for book in books:
                if book[1] == entry[1]:
                    book[3] = "Yes"
                # End if
            # End for
            return
        # End if
    # End for

    print("\nYou do not have that book borrowed.\n")
# End function

def show_all_by_user(books, borrowed, current_user):
    print()
    number_of_borrowed = 0

    for entry in borrowed:
        if entry[0] == current_user:
            for booker in books:
                if booker[1] == entry[0]:
                    print(f"You have {booker[1]} by {booker[2]} currently borrowed")    
                    number_of_borrowed +=1
                # End if
            # End for
        # End if
    # End for

    if number_of_borrowed == 0:
        print("You do not have any books borrowed.")
    # End if

    print()
    return
# End function

def Log_Out(books, borrowed):
    with open("books.csv", "w", newline="") as books_file:
        writer = csv.writer(books_file)

        for book in books:
            writer.writerow(book)
        # End for
    # End with

    with open("borrowed.csv", "w", newline="") as borrowed_file:
        writer = csv.writer(borrowed_file)

        for borrow in borrowed:
            writer.writerow(borrow)
        # End for
    # End with

    print("\nSucessfully Logged Out.")
    raise SystemExit(0)
# End function

def main():
    books, borrowed = load_files()
    print("\nWelcome to the Library of Dennis Wright")
    current_user = sign_in_or_up()

    keep_loop = True
    first_iteration = True

    while keep_loop:
        if first_iteration:
            first_iteration = False
        else:
            another_service = input("Would you like to use another service? (y/n) ").lower()
            if another_service != "y":
                Log_Out(books, borrowed)
        
        # Ask to use a service only if user wants to continue
        service_decider(books, borrowed, current_user)
# End function

main()