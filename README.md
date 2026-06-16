# 🏦 Simple CLI Bank Account System

A lightweight, interactive Command Line Interface (CLI) Code written in Python that simulates basic banking operations like checking balances, depositing funds, and withdrawing money with password verification.

---

## ✨ Features

* **Object-Oriented Design:** Built using a robust `BankAccount` class.
* **Password Protection:** Secure verification required before completing transactions.
* **Deposit Management:** Automatically checks for valid deposit amounts.
* **Withdrawal Safety Nets:** Prevents overdrafts and handles negative input values with a touch of humor.
* **Interactive Menu:** A continuous loop allowing users to perform multiple operations until they explicitly choose to exit.

---

## 🛠️ How It Works

### Core Logic Breakdown

1. **Initialization:** The account is created with an owner's name, a starting balance, and a secure PIN/password.
2. **Validation Checkpoints:**
   * **Deposits** must be ₹1 or greater.
   * **Withdrawals** cannot exceed the current available balance, nor can they be zero or negative values.
   * **Authentication:** The system asks for your password *every time* you try to move funds.

---

## 🚀 Running the Program

### Prerequisites
Make sure you have Python installed on your system. 

### Execution
1. Copy the code into a file named `bank.py`.
2. Open your terminal or command prompt and run:
   ```bash
   python bank.py

---
### Default Credentials
By default, the script initializes with a pre-configured account for testing:
* **Account Holder:** `Tester_Bro`
* **Starting Balance:** ₹2000
* **Password:** `123456`

---

### 🕹️ User Guide & Menu Prompts
When you run the application, you will be greeted by an interactive menu:

| Input Choice | Action | Description |
| :--- | :--- | :--- |
| **W / w** | Withdraw | Prompts for amount and password to withdraw cash. |
| **D / d** | Deposit | Prompts for amount and password to add cash. |
| **E / e** | Exit | Safely closes the application. |

---

### ⚠️ Special Responses (Easter Eggs)
The script features customized, humorous warning strings for edge-case errors:

* **Trying to withdraw ₹0 or negative money?**
  > *"Mazak Nhi Chalega, Zaada Masti Kari toh Bank Account Suspend Hojaega"*
* **Trying to withdraw more than your current balance?**
  > *"Beta,gareebi chal rahi hai, balance kam hai!"*