# THIS IS THE FORGOT PASSWORD MODULE
from utils.storage import load_accounts
from utils.storage import save_all_accounts
import getpass
import clear_terminal as ct
import hashlib
import time

# hash function (reuse same as in create_account)
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def forgot_password_function():
    ct.clear()
    print("=======================================================================") 
    print("========================= FORGOT PASSWORD =============================")
    print("=======================================================================") 

    username = input("Enter your user-name: ")

    accounts = load_accounts()
    account = next((acc for acc in accounts if acc["user_name"] == username), None)

    if not account:
        print("❌ No account found with that username.")
        input("Press Enter to return to the main menu...")
        return

    # Ask for email verification
    email_input = input("Enter your registered email: ")

    if email_input.lower() != account["email"].lower():
        print("❌ Email does not match our records.")
        input("Press Enter to return to the main menu...")
        return

    print("\n✅ User verified! You can now reset your PIN.\n")

    # PIN reset loop
    while True:
        new_pin = getpass.getpass("Enter new 4-digit PIN: ")

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("❌ Invalid PIN. Must be 4 digits.")
            continue

        confirm_pin = getpass.getpass("Confirm new PIN: ")

        if new_pin != confirm_pin:
            print("❌ PINs do not match. Try again.")
            continue

        # hash and save
        account["pin"] = hash_password(new_pin)
        break

    # Save changes back to JSON
    save_all_accounts(account)

    print("\n✅ PIN reset successfully!")
    time.sleep(2)
    input("Press Enter to return to the main menu...")
