import bcrypt
import utils
import json

def load_details():
    user_details = {}

    with open('data/users.json', 'r') as user_logins:
        try:
            logins = json.load(user_logins)
        except json.JSONDecodeError:
            logins = []

    for user in logins:
        user_details[user["username"]] = user["password"]

    return user_details

# STILL TO BE DONE.
def login(user_details):
    print()
# End function

def register(user_details):
    terminal_width = utils.get_width()

    bars = "=" * terminal_width
    main_text = "USER REGISTRATION"

    main_padding = utils.get_padding(terminal_width, len(main_text))

    print()
    print(bars)
    print(" " * main_padding + main_text)
    print(bars)

    while True:
        # Username input
        username_text = "ENTER USERNAME: "
        username_padding = utils.get_padding(terminal_width, len(username_text))
        print("\n" + " " * username_padding + username_text)

        input_prompt = "> "
        input_padding = (terminal_width - len(input_prompt)) // 2 - 9
        username_input = input(" " * input_padding + input_prompt).strip()

        if not username_input:
            print("Error: You must enter a username.")
            continue

        if username_input in user_details:
            print("Error: Username already exists.")
            continue 

        # Password input
        password_text = "ENTER PASSWORD: "
        password_padding = utils.get_padding(terminal_width, len(password_text))
        print("\n" + " " * password_padding + password_text)

        password_input = input(" " * input_padding + input_prompt).strip()
        if not password_input:
            print("Error: You must enter a password.")
            continue

        pswd = password_input.encode('utf-8')
        hashed_password = bcrypt.hashpw(pswd, bcrypt.gensalt())

        # If username not existing and valid password, write to array which will push to json file
        print(f"\nUser '{username_input}' registered successfully!")
        write_to_json(username_input, hashed_password, user_details)
        break
    # End while
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

    user_details = load_details()

    if function == "login":
        login(user_details)
    else:
        register(user_details)
# End function
