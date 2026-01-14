# 🗑️ File Shredder (Python)

A simple command-line file shredder I made to permanently delete files.  
It overwrites the file a few times, renames it a bunch of times, and then deletes it.  
Pretty much makes it hard to recover stuff, but still kinda basic.
This was my first time experimenting with argparse instead of input.

## ✨ Features

### 🔒 File Deletion
- Overwrites files multiple times with 0s, 1s, and random data  
- Truncates the file to 0 bytes after overwriting  
- Renames the file a bunch of times with random strings before deleting  

### 🖥️ Command Line Options
- `-f, --file` → The file you want to delete (required)  
- `-p, --passes` → How many times to overwrite (Can be unlimited, default 3, not really worth doing loads of passes tbh)  
- `--force` → Skip the “are you sure?” prompt  

### 📢 Feedback
- Prints each pass as it overwrites  
- Shows the new random file names as it renames  
- Prints when the file is finally deleted  

## 🧩 How the program works
- `parse_arguments()` → Gets the stuff you type in the command line  
- `confirm_overwrite()` → Asks if you really want to delete the file  
- `overwrite_file_content()` → Does the overwriting + truncating  
- `rename_file()` → Changes the filename a bunch of times  
- `delete_file()` → Deletes the file  

## ▶️ Running it
```bash
python fileshredda.py -f <file_path>
