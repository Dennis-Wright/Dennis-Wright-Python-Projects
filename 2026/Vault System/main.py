import os
import auth
import utils
import logging

def display_options(terminal_width):
    top_bottom = "=" * terminal_width

    option_1 = "[ 1 ]  LOGIN"
    option_2 = "[ 2 ]  REGISTER"
    option_3 = "[ 3 ]  EXIT"

    # Calculate spacing
    total_text_length = len(option_1) + len(option_2) + len(option_3)
    space_between = (width - total_text_length) // 4

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
        logging.info("Input Recieved: Login")
        auth.start("login")
    elif user_input == 2:
        logging.info("Input Recieved: Register")
        auth.start("register")
    elif user_input == 3:
        logging.info("Input Recieved: Program Exit")
        print()
        print(" " * left_padding + "Exiting Program")
        raise SystemExit(0)
    else:
        logging.warning(f"Invalid Input Recieved in Main Menu")
        print("\nInvalid option.\n")
        return get_input()
# End function

if __name__ == "__main__":
    utils.clear_screen()
    utils.configure_logging()
    width = utils.get_width()
    utils.display_banner()
    display_options(width)
    get_input()
