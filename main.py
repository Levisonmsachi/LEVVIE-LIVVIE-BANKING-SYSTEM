# this is the main file of the banking system

from authetication.login import login
from authetication.register import create_account
from authetication.forgot_password import forgot_password_function
from authetication.exit import exit_program
#from authetication.logout import logout
#from transactions.deposit import deposit
import clear_terminal as ct



def main():
    while True:
        ct.clear()
        print("=======================================================================") 
        print("=============== WELCOME TO LEVVIE-LIVVIE BANKING SYSTEM ===============")
        print("=======================================================================") 
        print("1. Create Account")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        print("=======================================================================") 
        print("=======================================================================") 

        try:
            choice = int(input("Choose an option: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue....")
            continue


        match choice:
            case 1:
                create_account()
                continue

            case 2:
                login()

            case 3:
                forgot_password_function()

            case 4:
                exit_program()

            case _:
                print("Invalid choice. Please try again. ")
                input("Press Enter to continue....")
                continue




if __name__ == "__main__":
    main()
