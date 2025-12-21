# 🏦 Banking System (Python + CSV)

A simple modular command–line banking system that simulates real account
operations. Includes login authentication, withdrawing, depositing, and balance
tracking - all backed by CSV files so accounts persist between sessions.

## ✨ Features

### 🔐 Login System
- Users log in using a username, account_number and pin
- Credentials stored in a CSV file
- Modular functions for authentication
- Prevents invalid login access

### 💰 Banking Operations
After login, users can:
- **Check balance**
- **Deposit money**
- **Withdraw money** (with balance validation)
- Update stored balance in the CSV

### 💾 Persistent Data (CSV)
The system stores accounts using:
username, account_number, pin, balance

## 🧩 Program Structure
- Modular functions for each action
- Input validation for numeric balances
- Repeated menu loop for multiple operations
- Exit cleanly when finished

## ▶️ Running the Program
```bash
python program.py
