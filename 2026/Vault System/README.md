# File Vault System (Python)

A modular command-line file vault application that allows users to securely register, log in, and manage personal files in an isolated vault. The system uses hashed passwords (`bcrypt`) and file operations to upload, view, delete, and download files — all stored locally per user.

---

## ✨ Features

### 🔐 Authentication
- Register new users with hashed passwords using `bcrypt`
- Log in securely with username and password
- Credentials stored in a JSON file (`data/users.json`)
- Each user gets a dedicated vault directory (`data/vaults/<username>`)

### 📁 Vault Operations
Once logged in, users can:
- View all files stored in their vault
- Upload files from their local machine into the vault
- Delete files from their vault
- Download files from the vault to a specified directory

All actions include input validation and user-friendly prompts.

---

## 📦 Project Structure
- `main.py` — Entry point for login and registration menus
- `auth.py` — Handles user authentication and registration
- `vault.py` — Implements file vault functionality
- `utils.py` — Utility functions (terminal formatting, screen clear, logging)
- `data/` — Contains user data and vault directories
  - `data/users.json` — Stores registered user credentials
  - `data/vaults/` — Contains vaults for each user

---

## 💻 Requirements
- Python 3.9+
- `bcrypt` (for secure password hashing)

Install dependencies:

```bash
pip install bcrypt
```

---

## ▶️ Running the Program

Start the application from the project root:

```bash
python main.py
```

Follow the menus to:

- Register a new account (if needed)
- Log in
- Manage your files in the vault

---

### 📷 Screenshots

**Login Screen:**
<img width="1905" height="280" alt="image" src="https://github.com/user-attachments/assets/7924075f-fb73-4754-a5e0-37ea441438a3" />


**Vault Interface:**
<img width="1904" height="326" alt="image" src="https://github.com/user-attachments/assets/ec6813a2-c770-4ba2-ab52-a7b77aa0c73d" />
  
---

## 🛠️ How It Works

- Passwords are hashed when stored and checked using `bcrypt`
- Vault files are stored separately per user in a dedicated directory
- Menus guide the user through available commands with input validation
- Logging is enabled to record operations in `logs/activity.log`

---

## 📌 Notes

- Designed for local personal use
- Not intended for production-level security (no encryption of files yet)
- Can be extended with encryption or networking features in future versions
