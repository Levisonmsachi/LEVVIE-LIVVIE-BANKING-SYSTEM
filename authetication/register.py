# THIS IS A BANKING SYSTEM MADE BY LEVISON MSACHI AKA LEVVIE-LIVVIE
# this is the register screen where you can create your account

from utils.storage import save_account
import getpass
import random
import clear_terminal as ct
import hashlib

# a function to generate account number
def generate_account_number():
    prefix = "265"  # must start with 265
    remaining_digits = 10 - len(prefix)
    suffix = "".join(str(random.randint(0, 9)) for _ in range(remaining_digits))
    return prefix + suffix

# a function to hash a password
def hash_password(password: str) -> str:
    # SHA-256 hashing
    return hashlib.sha256(password.encode()).hexdigest()


def create_account():
    while True:
        ct.clear()
        print("=======================================================================") 
        print("====================== CREATE ACCOUNT MENU ============================")
        print("=======================================================================") 

        f_name = input("Enter your first name: ")
        l_name = input("Enter your last name: ")
        user_name = input("Enter your user-name: ")
        email = input("Enter your email: ")
        account_type = input("Enter account type (Savings/Current): ")

        full_name = f"{f_name} {l_name}"

        # PIN input loop
        while True:
            pin = getpass.getpass("Set a 4-digit PIN: ")

            if len(pin) != 4 or not pin.isdigit():
                print("❌ Invalid PIN. Must be 4 digits (numbers only).")
                input("Press Enter to continue...")
                continue

            confirm_pin = getpass.getpass("Confirm your PIN: ")

            if confirm_pin != pin:
                print("❌ PINs do not match. Please try again.")
                input("Press Enter to continue...")
                continue

            # ✅ Success, break out of PIN loop
            break  

        # Hash the PIN before storing
        hashed_pin = hash_password(pin)
        pin = hashed_pin 
        

        # Generate account number
        account_number = generate_account_number()

        account_data = {
            "account_number": account_number,
            "user_name": user_name,
            "account_type": account_type,
            "full_name": full_name,
            "email": email,
            "pin": pin,   
            "balance": 0.0
        }

        save_account(account_data)  # save into storage

        print("\n✅ Account created successfully!")
        print(f"Your account number is: {account_number}")
        input("\nPress Enter to return to the main menu...")
        break  # exit create_account loop once account is made
