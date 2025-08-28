# function to exit the program
import clear_terminal as ct
import time

def exit_program():
    cont = input("Are you sure you want to exit? (yes/no): ").strip().lower()

    if cont in ["yes", "no"]:
        if cont == "yes":
            ct.clear()
            print("Exiting the program...")
            time.sleep(2)
            ct.clear()
            print("Thank you for using LEVVIE-LIVVIE banking system. Goodbye!")
            input("Press Enter to exit...")
            exit()

        elif cont == "no":
            return()

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        input("Press Enter to continue....")
        return()