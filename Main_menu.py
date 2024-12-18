import pickle
import shelve

# Define global variables
membership = {}
meetings = {}

# Define file names
membership_file = "membership.pkl"
meetings_file = "meetings.pkl"


def main_menu():
    while true:
        print("\nMain Menu:")
        print("1. Manage Memberships")
        print("2. Enter marks for a meeting")
        print("3. Retrive stats for a book")
        print("4. Exit")
        choice = input("Choose an option")

        if choice == "1":
            membership_menu()
        elif choice == "2":
            enter_marks()
        elif choice == "3":
            stats_menu()
        elif choice == "4":
            save_data()
            print("Exiting program")
            break
        else:
            print("Invalid option. Try again.")
        
