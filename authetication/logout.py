import time
import clear_terminal as ct

def logout_account(account):
    ct.clear()
    print(f"🔒 Logging out {account['full_name']}...")
    time.sleep(3)
    ct.clear()
    print("✅ You have been logged out successfully.")
    input("Press Enter to return to the main menu...")
    return  # return to main menu
