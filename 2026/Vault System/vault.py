import utils
import logging
import os
import shutil

def display_title(username):
    text = f"Welcome to your file vault {username}"
    text_padding = utils.get_padding(len(text))
    print("\n" + " " * text_padding + text)
# End function

def display_options():
    terminal_width = utils.get_width()

    top_bottom = "=" * terminal_width

    option_1 = "[ 1 ]  VIEW ALL FILES"
    option_2 = "[ 2 ]  UPLOAD A FILE"
    option_3 = "[ 3 ]  DELETE A FILE"
    option_4 = "[ 4 ]  DOWNLOAD A FILE"
    option_5 = "[ 5 ]  EXIT"

    # Calculate spacing
    total_text_length = len(option_1) + len(option_2) + len(option_3) + len(option_4) + len(option_5)
    space_between = (terminal_width - total_text_length) // 6

    line = (
        " " * space_between +
        option_1 +
        " " * space_between +
        option_2 +
        " " * space_between +
        option_3 +
        " " * space_between +
        option_4 +
        " " * space_between +
        option_5 +
        " " * space_between
    )

    print(top_bottom)
    print(line)
    print(top_bottom)
# End function

def get_input(username):
    prompt_text = "ENTER OPTION: "
    
    left_padding = utils.get_padding(len(prompt_text))

    try:
        user_input = int(input(" " * left_padding + prompt_text))
    except:
        print("Error. Invalid input.")
        get_input()

    if user_input == 1:
        logging.info("Vault.py - Input Recieved: ViewAll")
        view_all_files(username, "input")
    elif user_input == 2:
        logging.info("Vault.py - Input Recieved: Upload")
        upload_file(username)
    elif user_input == 3:
        logging.info("Vault.py - Input Recieved: Delete")
        delete_file(username)
    elif user_input == 4:
        logging.info("Vault.py - Input Recieved: Download")
        download_file(username)
    elif user_input == 5:
        logging.info("Vault.py - Input Recieved: Program Exit")
        print()
        print(" " * left_padding + "Exiting Program")
        raise SystemExit(0)
    else:
        logging.warning(f"Vault.py - Invalid Input Recieved")
        print("\nInvalid option.\n")
        return get_input()
# End function  

def view_all_files(username, source):
    display_text = f"YOUR FILES:"
    display_padding = utils.get_padding(len(display_text))
    print("\n" + " " * display_padding + display_text)
    files = os.listdir(f"data/vaults/{username}/")
    logging.info(f"Vault.py - Displaying all files in vault for user '{username}'")
    for filename in files:
        filename_padding = utils.get_padding(len(filename))
        print(" " * filename_padding + filename)

    if source == "input":
        another_service(username)
# End function

def upload_file(username):
    upload_text = "Enter the file you would like to upload"
    upload_text_padding = utils.get_padding(len(upload_text))
    print("\n" + " " * upload_text_padding + upload_text)

    arrow = "> "
    arrow_spacing = 20
    arrow_padding = utils.get_padding(len(arrow))-arrow_spacing
    file_path = str(input(" " * arrow_padding + arrow))

    while not file_path:
        print("Error. You must enter a file.")
        file_path = str(input(" " * arrow_padding + arrow))
    
    if not os.path.exists(file_path):
        print("Error. Enter a valid file path.")
        return another_service(username)
    
    file_name = os.path.basename(file_path)

    if os.path.exists(f"data/vaults/{username}/{file_name}"):
        print("Error. File already in vault.")
        return another_service(username)


    try:
        shutil.copy(file_path, f"data/vaults/{username}/")
        logging.info(f"vault.py - file {file_name} copied to data/vaults/{username}/{file_name} sucessfully.")
    except:
        print("Error Copying file.")
        logging.error(f"vault.py - error copying file {file_name} for {username}")
    
    if os.path.exists(f"data/vaults/{username}/{file_name}"):
        text = f"File {file_name} uploaded successfully."
        text_padding = utils.get_padding(len(text))
        print("\n" + " " * text_padding + text)

    another_service(username)
# End function

def delete_file(username):
    view_all_files(username, "delete")

    delete_text = "Enter the name of the file you would like to delete."
    delete_text_padding = utils.get_padding(len(delete_text))
    print("\n" + " " * delete_text_padding + delete_text)

    arrow = "> "
    arrow_spacing = 9
    arrow_padding = utils.get_padding(len(arrow))-arrow_spacing
    file_name = str(input(" " * arrow_padding + arrow))

    while not file_name:
        print("Error. You must enter a file.")
        file_name = str(input(" " * arrow_padding + arrow))
    
    if not os.path.exists(f"data/vaults/{username}/{file_name}"):
        print("Error. Enter a valid file.")
        return another_service(username)

    try:
        os.remove(f"data/vaults/{username}/{file_name}")
        logging.info(f"Vault.py - Delete file {file_name} for user '{username}'")
    except:
        print(f"Error. Could not delete {file_name}")
        logging.error(f"Vault.py - Could not delete file {file_name} for user '{username}'")
    
    if not os.path.exists(f"data/vaults/{username}/{file_name}"):
        text = f"{file_name} deleted successfully."
        text_padding = utils.get_padding(len(text))
        print("\n" + " " * text_padding + text)

    another_service(username)
# End function
    
def download_file(username):
    view_all_files(username, "download")

    download_text = "Enter the name of the file you would like to download to your system."
    download_text_padding = utils.get_padding(len(download_text))
    print("\n" + " " * download_text_padding + download_text)

    arrow = "> "
    arrow_spacing = 9
    arrow_padding = utils.get_padding(len(arrow))-arrow_spacing
    file_name = str(input(" " * arrow_padding + arrow))

    while not file_name:
        print("Error. You must enter a file.")
        file_name = str(input(" " * arrow_padding + arrow))
    
    if not os.path.exists(f"data/vaults/{username}/{file_name}"):
        print("Error. Enter a valid file.")
        return another_service(username)

    download_directory = "Enter the path of the directory you would like to download the file to"
    download_directory_padding = utils.get_padding(len(download_directory))
    print("\n" + " " * download_directory_padding + download_directory)

    arrow = "> "
    arrow_spacing = 20
    arrow_padding = utils.get_padding(len(arrow))-arrow_spacing
    directory_name = str(input(" " * arrow_padding + arrow))

    while not directory_name:
        print("Error. You must enter a download directory.")
        directory_name = str(input(" " * arrow_padding + arrow))

    if not os.path.isdir(directory_name):
        print("Error. Enter a valid directory.")
        return another_service(username)


    try:
        shutil.copy(f"data/vaults/{username}/{file_name}", directory_name)
        logging.info(f"Vault.py - {file_name} copied from data/vaults/{username}/{file_name} to {directory_name}")
    except:
        print(f"Error. Could not copy {file_name}")
        logging.error(f"Vault.py - Could not copy file {file_name} for user '{username}'")
    
    if os.path.exists(f"{directory_name}/{file_name}"):
        text = f"{file_name} downloaded successfully."
        text_padding = utils.get_padding(len(text))
        print("\n" + " " * text_padding + text)

    another_service(username)
# End function

def another_service(username):
    text = "Would you like to use another service? (y/n): "
    text_padding = utils.get_padding(len(text))
    another = str(input("\n" + " " * text_padding + text)).lower()

    if another == "y":
        logging.info(f"Vault.py - {username} selecting another service.")
        get_input(username)
    else:
        logging.info(f"Vault.py - {username} selected to exit, exiting.")
        print("Thank you for using the Vault Service. Exiting...")
        raise SystemExit(0)
# End function

def main(username):
    utils.clear_screen()
    utils.display_banner()
    display_title(username)
    display_options()
    get_input(username)
# End function
