import bcrypt
import utils
import json
import logging

def load_details():
    user_details = {}

    with open('data/users.json', 'r') as user_logins:
        try:
            logging.info("User json loaded successfully.")
            logins = json.load(user_logins)
        except (json.JSONDecodeError, FileNotFoundError):
            logging.error("User json loading failed.")
            logins = []

    for user in logins:
        user_details[user["username"]] = user["password"]

    return user_details
# End function

def login(user_details):
    logged_in = False

    terminal_width = utils.get_width()

    bars = "=" * terminal_width
    main_text = "LOGIN"

    main_padding = utils.get_padding(len(main_text))

    print()
    print(bars)
    print(" " * main_padding + main_text)
    print(bars)

    while True:
        # Username input
        username_text = "ENTER USERNAME: "
        username_padding = utils.get_padding(len(username_text))
        print("\n" + " " * username_padding + username_text)

        input_prompt = "> "
        PROMPT_OFFSET = 9
        input_padding = (terminal_width - len(input_prompt)) // 2 - PROMPT_OFFSET
        username_input = input(" " * input_padding + input_prompt).strip()

        if not username_input:
            print("Error: You must enter a username.")
            continue


        # Password input
        password_text = "ENTER PASSWORD: "
        password_padding = utils.get_padding(len(password_text))
        print("\n" + " " * password_padding + password_text)

        password_input = input(" " * input_padding + input_prompt).strip()
        if not password_input:
            print("Error: You must enter a password.")
            continue

        if username_input not in user_details:
            print("Error: Invalid Username or Password.")
            continue 

        if bcrypt.checkpw(password_input.encode("utf-8"), user_details[username_input].encode("utf-8")):
            logging.info(f"Successful login attempt for user '{username_input}'")
            correct_text = "CORRECT. LOGGING IN..."
            correct_padding = utils.get_padding(len(correct_text))
            print("\n" + " " * correct_padding + correct_text)
            logged_in = True
        else:
            logging.warning(f"Failed login attempt for user '{username_input}'")
            print("Error: Invalid Username or Password.")
            logged_in = False
            continue

        break
    # End while

    return logged_in, username_input
# End function

def register(user_details):
    logged_in = False

    terminal_width = utils.get_width()

    bars = "=" * terminal_width
    main_text = "USER REGISTRATION"

    main_padding = utils.get_padding(len(main_text))

    print()
    print(bars)
    print(" " * main_padding + main_text)
    print(bars)

    while True:
        # Username input
        username_text = "ENTER USERNAME: "
        username_padding = utils.get_padding(len(username_text))
        print("\n" + " " * username_padding + username_text)

        input_prompt = "> "
        PROMPT_OFFSET = 9
        input_padding = (terminal_width - len(input_prompt)) // 2 - PROMPT_OFFSET
        username_input = input(" " * input_padding + input_prompt).strip()

        if not username_input:
            print("Error: You must enter a username.")
            continue

        if username_input in user_details:
            logging.warning(f"Registration failed as user '{username_input}' already exists.")
            print("Error: Username already exists.")
            continue 

        # Password input
        password_text = "ENTER PASSWORD: "
        password_padding = utils.get_padding(len(password_text))
        print("\n" + " " * password_padding + password_text)

        password_input = input(" " * input_padding + input_prompt).strip()
        if not password_input:
            print("Error: You must enter a password.")
            continue

        confirm_text = "CONFIRM PASSWORD: "
        confirm_padding = utils.get_padding(len(confirm_text))
        print("\n" + " " * confirm_padding + confirm_text)
        confirm_password = input(" " * input_padding + input_prompt).strip()

        if not confirm_password:
            print("Error: You must confirm your password.")
            continue

        if password_input != confirm_password:
            print("Error. Passwords do not match.")
            continue

        pswd = password_input.encode('utf-8')
        hashed_password = bcrypt.hashpw(pswd, bcrypt.gensalt())

        # If username not existing and valid password, write to array which will push to json file
        logging.info(f"User '{username_input}' registered successfully.")
        print(f"\nUser '{username_input}' registered successfully!")
        write_to_json(username_input, hashed_password, user_details)
        logged_in = True
        break
    # End while

    return logged_in, username_input
# End function

def write_to_json(username, password, user_details):
    user_details[username] = password.decode("utf-8")
    users_list = [{"username": u, "password": p} for u, p in user_details.items()]
    with open('data/users.json', 'w') as file:
        json.dump(users_list, file, indent=4)
# End function

def start(function):
    utils.clear_screen()
    utils.display_banner()
    utils.configure_logging()

    user_details = load_details()

    if function == "login":
        logged_in, username = login(user_details)
    else:
        logged_in, username = register(user_details)
# End function
