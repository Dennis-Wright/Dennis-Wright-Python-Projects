import os
import auth
import utils

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

def get_input(terminal_width):
    prompt_text = "ENTER OPTION: "
    
    left_padding = utils.get_padding(terminal_width, len(prompt_text))-1

    try:
        user_input = int(input(" " * left_padding + prompt_text))
    except:
        print("Error. Invalid input.")
        raise SystemExit(1)

    if user_input == 1:
        auth.start("login")
    elif user_input == 2:
        auth.start("register")
    elif user_input == 3:
        print()
        print(" " * left_padding + "Exiting Program")
        raise SystemExit(0)
    else:
        print("\nInvalid option.\n")
        return get_input(terminal_width)
# End function

if __name__ == "__main__":
    utils.clear_screen()
    width = utils.get_width()
    utils.display_banner()
    display_options(width)
    get_input(width)
