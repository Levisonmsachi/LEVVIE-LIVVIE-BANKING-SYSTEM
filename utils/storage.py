# utils/storage.py
import json
import os

DB_FILE = "accounts.json"

def load_accounts():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_account(updated_account):
    accounts = load_accounts()
    
    # Try to find the existing account
    for i, acc in enumerate(accounts):
        if acc["user_name"] == updated_account["user_name"]:
            accounts[i] = updated_account  # update the existing account
            break
    else:
        # If account not found, append as new
        accounts.append(updated_account)

    # Write the updated accounts list back to the file
    with open(DB_FILE, "w") as f:
        json.dump(accounts, f, indent=4)


# forgot password
def save_all_accounts(account_to_update):
    accounts = load_accounts()

    for i, acc in enumerate(accounts):
        if acc["user_name"] == account_to_update["user_name"]:
            accounts[i] = account_to_update
            break
    else:
        print("❌ Account not found. Cannot update.")
        input("Press Enter to return to the main menu...")
        return

    with open(DB_FILE, "w") as f:
        json.dump(accounts, f, indent=4)
