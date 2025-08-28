# THIS IS THE HISTORY MODULE
import clear_terminal as ct
import time

def view_history(account):
    ct.clear()
    print("=======================================================================") 
    print(f"==================== TRANSACTION HISTORY - {account['full_name']} ====================")
    print("=======================================================================") 
    
    if not account.get("history") or len(account["history"]) == 0:
        print("\n📭 No transaction history found.")
    else:
        for idx, txn in enumerate(account["history"], start=1):
            print(f"{idx}. {txn['time']} | {txn['type']}: ${txn['amount']:.2f} | Balance: ${txn['balance']:.2f}")
    
    input("\nPress Enter to return to your account menu...")
