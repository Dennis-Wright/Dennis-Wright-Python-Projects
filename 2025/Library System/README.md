# 📚 Library Management System (Python + CSV)

A command–line library system that supports login, viewing available books,
searching, borrowing, returning, and tracking borrowed books by user.  
All storage is handled using CSV files so data persists between runs.

## ✨ Features

### 🔐 User Authentication
- Sign-in and sign-up supported
- Username stored in `logins.csv`
- Password validation (A–Z, a–z, 0–9)
- Password encrypted before storing

### 📖 Book & Borrow Management
- View all books in the library
- Search by **title and author**
- Borrow only if available
- Return only if the current user has it
- Track borrowed items per user

### 💾 CSV Files Used
**books.csv**
ID,Title,Author,Available

**borrowed.csv**
username,title

**logins.csv**
username,encrypted_password

## 🧩 Program Flow
1. Load CSV files
2. Sign in or sign up
3. Display main service menu
4. Perform chosen action
5. Ask whether to continue after each action
6. Save CSV updates on logout

## ▶️ How to Run
```bash
python main.py
