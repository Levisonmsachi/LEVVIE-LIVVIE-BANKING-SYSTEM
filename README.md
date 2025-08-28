# 🏦 LEVVIE-LIVVIE BANKING SYSTEM

![Banking System Screenshot](https://github.com/Levisonmsachi/LEVVIE-LIVVIE-BANKING-SYSTEM/blob/main/utils/Screenshot_2025-08-28_08_20_33.png)

[![Python Version](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Last Commit](https://img.shields.io/github/last-commit/Levisonmsachi/LEVVIE-LIVVIE-BANKING-SYSTEM)](https://github.com/Levisonmsachi/LEVVIE-LIVVIE-BANKING-SYSTEM/commits/main)

A **futuristic and professional Python-based Banking System** by **Levison Msachi (LEVVIE-LIVVIE)**.  
Simulates a real banking application where users can register, log in, deposit, withdraw, transfer funds, and view transaction history.

---

## 🚀 Features

- **User Authentication**
  - Create accounts with unique username, email, and 4-digit PIN.
  - Secure PIN storage using SHA-256 hashing.
  - Forgot PIN functionality for easy password reset.
- **Account Management**
  - Check balance in real-time.
  - Deposit and withdraw funds securely.
  - Send money to other users using username & account number.
- **Transaction History**
  - View a detailed log of all deposits, withdrawals, and transfers.
- **Professional & Futuristic UI**
  - Clean terminal interface.
  - Clear prompts, error handling, and confirmations.
  - Elegant and consistent user experience.

---

## 🎬 Demo

Here’s how the system looks in action:

=======================================================================
====================== LOGIN MENU =====================================
Enter your user-name: levis
Enter your 4-digit PIN: ****

=============✅ Welcome back, Levison Msachi!=================

Check balance

Deposit

Withdraw

Send money

Logout
=======================================================================

Your account balance is: $1500.00

yaml
Copy code


---

## 🛠️ Technologies Used

- Python 3
- JSON for local data storage
- Terminal-based UI using `clear_terminal` and structured prompts
- SHA-256 hashing for secure PIN storage

---

## 💻 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/Levisonmsachi/LEVVIE-LIVVIE-BANKING-SYSTEM.git
cd LEVVIE-LIVVIE-BANKING-SYSTEM
Run the main script

bash
Copy code
python3 main.py
Follow the on-screen prompts to create an account, log in, and manage your funds.

🧩 File Structure
pgsql
Copy code
Banking-System/
│
├── authetication/       # Login, register, logout, forgot_password
├── transactions/        # Deposit, Withdraw, Transfer modules
├── utils/               # Storage, clear_terminal, screenshot
├── accounts.json        # Local storage for user accounts
├── main.py              # Entry point of the application
└── README.md
⚠️ Notes
All data is stored locally in accounts.json.

PINs are hashed for security but this is not production-level.

Designed for educational purposes and learning Python project structures.

🌟 Author
Levison Msachi (LEVVIE-LIVVIE)
GitHub: @Levisonmsachi

Give it a ⭐ if you like the project! 💙
