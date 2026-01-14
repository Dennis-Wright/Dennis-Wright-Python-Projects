import os
import secrets
import string
import random
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="File Shredder - by Dennis Wright")
    parser.add_argument("-f", "--file", required=True, help="Path to the file to shred")
    parser.add_argument("-p", "--passes", type=int, default=3, help="Number of overwrite passes (default: 3)")
    parser.add_argument("--force", action="store_true", help="Skip confirmation prompt")
    return parser.parse_args()
# End function

def confirm_overwrite(file):
    are_you_sure = input(f"You are about to permanently delete '{file}'. Continue? (y/n) ")
    if are_you_sure.lower() != "y":
        print("\nOperation cancelled.")
        sys.exit(0)
# End function

def overwrite_file_content(file, passes):
    file_size_in_bytes = os.path.getsize(file)
    overwrite_patterns = [b"\x00", b"\xFF", None]

    try:
        with open(file, "r+b", buffering=0) as binary_file:
            for current_pass in range(passes):
                binary_file.seek(0)
                current_pattern = overwrite_patterns[current_pass % len(overwrite_patterns)]

                if current_pattern is None:
                    overwrite_data = secrets.token_bytes(file_size_in_bytes)
                else:
                    overwrite_data = current_pattern * file_size_in_bytes

                binary_file.write(overwrite_data)
                binary_file.flush()
                os.fsync(binary_file.fileno())
                print(f"Pass {current_pass + 1}/{passes} complete.")
    except OSError as e:
        print(f"Error overwriting file: {e}")
        sys.exit(1)

    try:
        with open(file, "r+b") as binary_file:
            binary_file.truncate(0)
            binary_file.flush()
            os.fsync(binary_file.fileno())
        print("File truncated to 0 bytes successfully.")
    except OSError as e:
        print(f"Error truncating file: {e}")
        sys.exit(1)
# End function

def rename_file(file):
    number_of_renames = random.randint(10, 20)
    current_name = file
    file_directory = os.path.dirname(current_name)
    characters = string.ascii_letters + string.digits

    for index in range(number_of_renames):
        random_string = "".join(random.choice(characters) for _ in range(16))
        new_name = os.path.join(file_directory, random_string)
        try:
            os.rename(current_name, new_name)
            current_name = new_name
            print(f"File renamed to {new_name}")
        except OSError as e:
            print(f"Error renaming file on iteration {index + 1}: {e}")
            sys.exit(1)

    return current_name
# End function

def delete_file(file):
    try:
        os.remove(file)
        print(f"File '{file}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    args = parse_arguments()

    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' does not exist.")
        sys.exit(1)

    if not args.force:
        confirm_overwrite(args.file)

    print("\n========== STARTING FILE SHREDDER ==========\n")
    overwrite_file_content(args.file, args.passes)
    final_file = rename_file(args.file)
    delete_file(final_file)
    print("\n========== FILE SHREDDING COMPLETE ==========")
# End function
