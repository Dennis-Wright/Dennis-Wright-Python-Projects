# 🗑️ File Shredder (Python)

A simple command-line file shredder I made to permanently delete files **or entire directories**.  
It overwrites files a few times, renames them a bunch of times, and then deletes them.  
For directories, it goes through all files and subfolders and shreds everything bottom-up.  
Pretty much makes it hard to recover stuff, but still kinda basic.  
This was my first time experimenting with `argparse` instead of just `input`.

⚠ Note: This isn’t some super pro secure shredder, especially on SSDs — data might still be recoverable.  
I made this mostly to practice Python file I/O, directory traversal, and messing around with binary files.

## ✨ Features

### 🔒 File & Directory Deletion
- Overwrites files multiple times with 0s, 1s, and random data  
- Truncates files to 0 bytes after overwriting  
- Renames files a bunch of times with random strings before deleting  
- Directories: deletes all files first, then subfolders, then the directory itself  
- Prints warnings if a directory can’t be fsynced on Linux (POSIX)  

### 🖥️ Command Line Options
- `-f, --file` → The file you want to delete  
- `-d, --directory` → The directory you want to delete (all files inside will also be shredded)  
- `-p, --passes` → How many times to overwrite (default 3, can be higher but not really worth it)  
- `--force` → Skip the “are you sure?” confirmation prompt  

### 📢 Feedback
- Prints each pass as it overwrites  
- Shows new random file names as they are renamed  
- Prints when files or directories are finally deleted  
- Prints warnings if a directory fsync fails  

## 🧩 How the program works
- `parse_arguments()` → Gets the stuff you type in the command line  
- `validate_path()` → Checks that the file/directory exists and is valid  
- `confirm_overwrite()` → Asks if you really want to delete the target  
- `overwrite_file_content()` → Overwrites file contents + truncates them  
- `rename_file()` → Renames files randomly multiple times  
- `delete_file()` → Deletes the file  
- `shred_file()` → Wraps file overwrite + rename + delete (used by directories too)  
- `overwrite_dir()` → Traverses directories bottom-up, shredding all files and removing subfolders  

## ▶️ Running it

Delete a file:
```bash
python fileshredda.py -f <file_path>
```
Delete a directory:
```bash
python fileshredda.py -d <directory_path>
```
With custom overwrite passes and skipping confirmation:
```bash
python fileshredda.py -d <directory_path> -p 5 --force
```
