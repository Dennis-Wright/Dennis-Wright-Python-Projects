import time
import auth
import utils
import logging
import vault

def display_options():
    terminal_width = utils.get_width()

    top_bottom = "=" * terminal_width

    option_1 = "[ 1 ]  LOGIN"
    option_2 = "[ 2 ]  REGISTER"
    option_3 = "[ 3 ]  EXIT"

    # Calculate spacing
    total_text_length = len(option_1) + len(option_2) + len(option_3)
    space_between = (terminal_width - total_text_length) // 4

    line = (
        " " * space_between +
        option_1 +
        " " * space_between +
        option_2 +
        " " * space_between +
        option_3 +
        " " * space_between
    )

    print()
    print(top_bottom)
    print(line)
    print(top_bottom)
# End function

def get_input():
    prompt_text = "ENTER OPTION: "
    
    left_padding = utils.get_padding(len(prompt_text))-1

    try:
        user_input = int(input(" " * left_padding + prompt_text))
    except:
        print("Error. Invalid input.")
        raise SystemExit(1)

    if user_input == 1:
        logging.info("main.py - Input Recieved: Login")
        logged_in, username = auth.start("login")
    elif user_input == 2:
        logging.info("main.py - Input Recieved: Register")
        logged_in, username = auth.start("register")
    elif user_input == 3:
        logging.info("main.py - Input Recieved: Program Exit")
        print()
        print(" " * left_padding + "Exiting Program")
        raise SystemExit(0)
    else:
        logging.warning(f"main.py - Invalid Input Recieved")
        print("\nInvalid option.\n")
        return get_input()
    
    return logged_in, username
# End function

if __name__ == "__main__":
    utils.clear_screen()
    utils.configure_logging()
    utils.display_banner()
    display_options()
    logged_in, username = get_input()

    time.sleep(2)

    if logged_in:
        vault.main(username)
    else:
        logging.error("User not logged in, exiting program.")
        raise SystemExit(1)
