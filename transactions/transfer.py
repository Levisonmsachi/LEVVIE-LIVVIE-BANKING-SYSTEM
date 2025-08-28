# THIS IS THE TRANSFER MODULE
from utils.storage import load_accounts, save_account
import clear_terminal as ct
import time

def send_money(account):
    while True:
        ct.clear()
        print("=======================================================================") 
        print(f"==================== SEND MONEY - {account['full_name']} ====================")
        print("=======================================================================") 

        try:
            recipient_username = input("Enter recipient's user-name: ")
            recipient_acc_number = input("Enter recipient's account number: ")

            # Prevent sending to self
            if recipient_username == account["user_name"] and recipient_acc_number == account["account_number"]:
                print("❌ You cannot send money to yourself.")
                input("Press Enter to try again...")
                continue

            accounts = load_accounts()
            recipient = next(
                (acc for acc in accounts if acc["user_name"] == recipient_username and acc["account_number"] == recipient_acc_number),
                None
            )

            if not recipient:
                print("❌ Recipient not found or details incorrect. Please check username and account number.")
                input("Press Enter to try again...")
                continue

            try:
                amount = float(input("Enter amount to send: $"))
            except ValueError:
                print("❌ Invalid amount. Please enter a numeric value.")
                input("Press Enter to try again...")
                continue

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                input("Press Enter to try again...")
                continue

            if amount > account["balance"]:
                print("❌ Insufficient funds for this transfer.")
                input("Press Enter to try again...")
                continue

            # Deduct from sender
            account["balance"] -= amount

            # Add to recipient
            recipient["balance"] += amount

            # Save both accounts
            save_account(account)
            save_account(recipient)

            print(f"\n✅ Transfer successful! You sent ${amount:.2f} to {recipient['full_name']}.")
            print(f"Your new balance: ${account['balance']:.2f}")
            input("Press Enter to return to your account menu...")
            break

        except Exception as e:
            print(f"❌ An unexpected error occurred: {str(e)}")
            input("Press Enter to try again...")
