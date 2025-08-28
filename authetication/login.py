# THIS IS A BANKING SYSTEM MADE BY LEVISON MSACHI AKA LEVVIE-LIVVIE
# login screen with 3 PIN attempts
from transactions.withdraw import withdraw_funds
from utils.storage import load_accounts
import getpass
import clear_terminal as ct
import hashlib
import time
from authetication.logout import logout_account
from transactions.deposit import deposit_funds
from transactions.transfer import send_money


# hash function (same as create_account)
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# a function to display the menu after login success
def login_menu(account):
    while True:
        ct.clear()
        print("=======================================================================") 
        print(f"=============✅ Welcome back, {account['full_name']}!=================")
        print("=======================================================================")
        print("1. Check balance")
        print("2. Check account details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Send money")
        print("6. Logout")
        print("=======================================================================\n")

        try:
            choice = int(input("Choose an option: "))

            match choice:
                case 1:
                    print(f"Your account balance is: ${account['balance']:.2f}")
                    input("\nPress Enter to continue...")
                    continue

                case 2:
                    print("=======================================================================")
                    print(f"================== Your account details are:==========================")
                    print("=======================================================================")
                    print(f"Full Name:      {account['full_name']}")
                    print(f"Email:          {account['email']}")
                    print(f"Account Type:   {account['account_type']}")
                    print(f"Account Number: {account['account_number']}")
                    print(f"Balance:        ${account['balance']:.2f}")
                    print("=======================================================================\n")

                    input("\nPress Enter to continue...")
                    continue
  
                case 3:
                    deposit_funds(account)

                case 4:
                    withdraw_funds(account)

                case 5:
                    send_money(account)

                case 6:
                    confirm = input("Are you sure you want to logout? (yes/no): ")
                    if confirm.lower() == "yes":
                        logout_account(account)
                        return  # return to login() → then main menu
                    else:
                        continue

                case _:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
                    continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
            continue


def login():
    ct.clear()
    print("=======================================================================") 
    print("=========================== LOGIN MENU =================================")
    print("=======================================================================") 

    user_name = input("Enter your user-name: ")

    accounts = load_accounts()
    account = next((acc for acc in accounts if acc["user_name"] == user_name), None)

    if not account:
        print("❌ User not found. Please check your user-name.")
        input("Press Enter to return to main menu...")
        return  # back to main menu

    # allow up to 3 PIN attempts
    attempts = 3
    while attempts > 0:
        pin_input = getpass.getpass("Enter your 4-digit PIN: ")

        if len(pin_input) != 4 or not pin_input.isdigit():
            print("❌ Invalid PIN format. Please enter a 4-digit PIN.")
            continue

        hashed_input = hash_password(pin_input)

        if hashed_input == account["pin"]:
            # ✅ Successful login
            print(f"\n✅ Login successful! Welcome, {account['full_name']}!")
            print("Loading. Please wait...")
            time.sleep(2)
            login_menu(account)  # returns here after logout

            return  # return immediately to main menu after logout

        else:
            attempts -= 1

            if attempts > 0:
                print(f"❌ Incorrect PIN. You have {attempts} attempt(s) remaining.")

            else:
                print("❌ Too many incorrect attempts. Returning to main menu.")

            input("Press Enter to continue...")


