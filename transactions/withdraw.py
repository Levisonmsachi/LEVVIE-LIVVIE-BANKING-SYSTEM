# THIS IS THE WITHDRAW MODULE
from utils.storage import save_account
import clear_terminal as ct
import time

def withdraw_funds(account):
    while True:
        ct.clear()
        print("=======================================================================") 
        print(f"==================== WITHDRAW FUNDS - {account['full_name']} ====================")
        print("=======================================================================") 

        try:
            amount = float(input("Enter amount to withdraw: $"))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                input("Press Enter to try again...")
                continue

            if amount > account["balance"]:
                print("❌ Insufficient funds. Your current balance is " 
                      f"${account['balance']:.2f}.")
                input("Press Enter to try again...")
                continue

            # update balance for the logged-in account only
            account["balance"] -= amount

            # save the updated account
            save_account(account)

            print(f"\n✅ Withdrawal successful! New balance: ${account['balance']:.2f}")
            input("Press Enter to return to your account menu...")
            break

        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")
            input("Press Enter to try again...")
