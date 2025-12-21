# 🔐 Basic Encrypted Password Login App (Python + CSV)

A simple proof-of-concept login system demonstrating account creation,
password encryption, and authentication using CSV files. Fully modular
design, ideal for learning and testing basic login logic.

## ✨ Features

### 🧑‍💻 Sign In / Sign Up
- Check if a username exists in the CSV database
- If it exists, prompts for password and authenticates
- If it doesn’t exist, allows the user to sign up
- Modular functions for login logic

### 🔒 Password Encryption
- Passwords are encrypted before being stored
- Encryption uses a mix of letter/digit transformations:
  - Lowercase letters reversed
  - Uppercase letters shifted
  - Digits reversed
- Comparison always happens with encrypted data

### 💾 Persistent Data (CSV)
Stores credentials in `logins.csv`:
username,encrypted_password

## 🧩 Program Structure
- Modular code separated into:
  - `sign_in_or_up()`
  - `sign_in()`
  - `sign_up()`
  - `encrypt_password()`
- Easy to expand for more features
- Looping menu logic for repeated login attempts

## ▶️ Running the Program
```bash
python program.py
