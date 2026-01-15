import os
import secrets
import string
import random
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="File Shredder - by Dennis Wright")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Path to the file to shred")
    group.add_argument("-d", "--directory", help="Path to the directory to shred")

    parser.add_argument("-p", "--passes", type=int, default=3, help="Number of overwrite passes (default: 3)")
    parser.add_argument("--force", action="store_true", help="Skip confirmation prompt")
    return parser.parse_args()
# End function

def validate_path(path, expected_type):
    if not os.path.exists(path):
        print(f"Error: '{path}' does not exist.")
        sys.exit(1)
    
    if expected_type == "file" and not os.path.isfile(path):
        print(f"Error: '{path}' is not a valid file.")
        sys.exit(1)
    elif expected_type == "directory" and not os.path.isdir(path):
        print(f"Error: '{path}' is not a valid directory.")
        sys.exit(1)
    
    return path
# End function

def confirm_overwrite(path, expected_type):
    if expected_type == "directory":
        are_you_sure = input(f"You are about to permanently delete '{path}' and all files/subdirectories in it. Continue? (y/n) ")
    elif expected_type == "file":
        are_you_sure = input(f"You are about to permanently delete '{path}'. Continue? (y/n) ")
    
    if are_you_sure.lower() != "y":
        print("\nOperation cancelled.")
        sys.exit(0)
# End function

## Below this line is the code for directory

def overwrite_dir(path, passes):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            shred_file(os.path.join(root, name), passes)
        
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)
            fsync_dir(root)
    
    os.rmdir(path)
    fsync_dir(os.path.dirname(path) or ".")
# End function

def fsync_dir(path):
    if os.name == "posix":
        try:
            fd = os.open(path, os.O_DIRECTORY)
            os.fsync(fd)
            os.close(fd)
        except OSError as e:
            print(f"Warning: could not fsync directory '{path}': {e}")
# End function

## Below this line is the code for file

def shred_file(path, passes):
    overwrite_file_content(path, passes)
    final_file = rename_file(path)
    delete_file(final_file)
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
# End function





## MAIN


if __name__ == "__main__":
    args = parse_arguments()

    if args.file:
        path = args.file
        expected_type = "file"
    elif args.directory:
        path = args.directory
        expected_type = "directory"

    print(path, expected_type)

    path = validate_path(path, expected_type)

    print("\n========== STARTING FILE SHREDDER ==========\n")

    if not args.force:
        confirm_overwrite(path, expected_type)

    if expected_type == "directory":
        overwrite_dir(path, args.passes)
    else:
        shred_file(path, args.passes)

    print("\n========== FILE SHREDDING COMPLETE ==========")
