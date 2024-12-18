import pickle
import shelve

# Define global variables
membership = {}
meetings = {}

# Define file names
membership_file = "membership.pkl"
meetings_file = "meetings.pkl"


# Functions to save data to files
def save_data():
    with open(membership_file, "wb") as f: # open the membership file
              pickle.dump(membership, f) # Save into membership
    with open(meetings_file, "wb") as f: # Open meetings file
              pickle.dump(meetings, f) # Save into meetings
    print("Data saved successfuly.") # Print a message to the user to confrim file has been saved

# Function to load data from files
def load_data():
    global membership, meetings # Refering to global variables created earlier
    try:
        with open(membership_file, "rb")as f: # open membership file
            membership = pickle.load(f)
    except FileNotFoundError: # Error if file does not exist
        membership = {} # Initialize empty dictionary if file is not found
    try: # Do same as membership file for meetings file
        with open(meetings_file, "rb") as f:
            meetings = pickle.load(f)
    except FileNotFoundError:
            meetings = {}

            
# Function for main menu
def main_menu():
    while True:
        print("\nMain Menu:")# Title for main menu
        print("1. Manage Memberships")# Option to edit memberships
        print("2. Enter marks for a meeting")# Option to add marks for a meeting
        print("3. Retrive stats for a book and for members")# Option to vieew marks from previous meetings/books
        print("4. Exit")# Option to exit the program
        choice = input("Choose an option: ")

        if choice == "1":
            membership_menu()# call a function for membership menu
        elif choice == "2":
            enter_marks()# Call a function to enter marks
        elif choice == "3":
            stats_menu() # call a function to view stats
        elif choice == "4":
            save_data() # Call a function to save the data
            print("Exiting program")# Mesage when exiting the peogram
            break # End the loop
        else:
            print("Invalid option. Try again.") # Error message if an invalid option is selected

# Function for membership menu
def membership_menu(): 
    while True:
        print("\nMembership Menu:") # Create menu for membership menu with differnet options for user
        print("1. Add Member")
        print("2. Withdraw Member")
        print("3. Reinstate Member")
        print("4. Create New Book Club")
        print("5. Return To Main Menu")
        choice = input("Choose an option: ")

        if choice == "1": # Create a loop similiar for the main menu where each option corresponds to a function
            add_member()
        elif choice == "2":
            withdraw_member()
        elif choice == "3":
            reinstate_member()
        elif choice == "4":
            create_new_book_club()
        elif choice == "5":
            print("Returning to Main Menu")
            break
        else:
            print("Invalid option. Try again.")


# Function to add a member
def add_member():
    global membership
    name = input("Enter new member's name: ").strip()
    original_name = name # create new variable so names can be edited later on
    suffix = 1 # To help if any names are duplicates

    # check to see if name already exists
    while name in membership:
        name = original_name + "_" + str(suffix)
        suffix += 1 # If the name already exists in the list add 1 to the end of the name

    membership[name] = {"status": "active", "join_date": "today", "leave_date": None }
    print("Memeber '" + str(name) + "' has been added.")

#Function to remove a name from the list
def withdraw_member():
    global membership
    name = input("Enter the name of the member you would like to withdraw ") # Prompt user to enter name they would like to remove
    if name in membership and membership[name]["status"] == "active": # Check to see if the name is in the list and is an 'active' member
        membership[name]["status"] = "inactive" # Change membership status to inactive
        membership[name]["leave_date"] = "today" # Change the leave date to 'today'
        print("Member '" + name + "' has been removed") # Confirm to the user that the name has been removed
    else:
        print("Member has not been found or has already been removed.") # For names that are not in the list or have already been removed

#Function to reinstate a member
def reinstate_member():
    global membership
    name = input("Enter the name of the member you want to rienstate")
    if name in membership and membership[name]["status"] == "inactive": # Check if name is in the list and has been removed previously
        membership[name]["status"] = "active" # Change status to 'active'
        membership[name]["leave_date"] = None # Remove leave date
        print( "Member '" + name + "'has been reinstated")# Confirm to user that member has been reinstated
    else:
        print ("Member '" + name + "' is not in the list or has not been removed")

# Function to create a new book club
def create_new_book_club():
        global membership, meetings
        confirm = input("Please confirm that you want to create a new book club? (Enter 'yes' or 'no') This will remove all current data. ").strip()
        if confirm == "yes":
            membership = {} # Reset membership list
            meetings = {} # Reset meetings list
            save_data() # Save the new lists
            print("New book club has been created successfully") # Confirm to the user that the new book club has been created
        else:
            print("Keeping current book club")


# Function for entering the marks for meetings
def enter_marks():
    global meetings, membership
    book = input("Enter book title: ").strip() # Prompt user to enter name of the book
    author = input("Enter the name of the author: ") # Prompt user to enter the name of the author
    genre = input("Enter the genre (horror/sci-fi/fantasy/post-apocalyptic): ") # Prompt user to enter the genre of the book

    scores = {} # set up empty dictionary for scores
    for member, details in membership.items():
        if details["status"] == "active": # Check if the member is active
            score = input("Enter score for " + member + " (leave blank for missing): ").strip # Prompt user to enter the score
            scores[member] = float(score) if score else None # Store the scores in a new dictionary with the members name, store 'None' if no score is entered



if __name__ == "__main__":
    main_menu()
        
