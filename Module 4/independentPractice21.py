# Zachary Hoover || 10-10-23 || Independent Practice #21

# Imports
import os
import string

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

print_header("K-Pop")

def member_albums(member_name, num_albums):
    """Checks if bothe the name and album number are valid and prints a message."""
    try:
        # Check if the name entered is a string, if not, raise an error
        if type(member_name) != str:
            raise TypeError("Invalid name entered.")
        # Check if the number entered is negative, if it is, raise an error
        if num_albums < 0:
            raise ValueError("Invalid number of albums entered.")
    except (TypeError, ValueError) as ex:
        print("The program ran into an error!")
        raise ex
    finally:
        print("Function member_albums has finished execution.")
    
# Get inputs from user
try:
    name = str(input("Enter your name: "))
    num_albums = int(input("Enter number of albums: "))
except ValueError as ve:
    print(ve)

# Call function with inputs
member_albums(name, num_albums)
    
input("\n Press Enter to Continue...")
print_header("Cuisine")

def indian_menu_food(menu):
    """Checks the menu(dictionary) passed in for missing values, and raises a ValueError."""
    try:
        # loop through each menu item
        for menu_item, price in menu.items():
            # Check if the menu item is invalid
            if price == None or price <= 0:
                # Raise an exception for the menu item
                raise ValueError(f"The price for menu item {menu_item} is invalid.")
    except ValueError as ve:
        # Print a message and re-raise the exception
        print("The program ran into an error.")
        raise ve
    finally:
        # Print a message after other code
        print("Function check_menu has finished running")
        
try:
    # Create the dictionary of foods
    indian_food_menu = {
        'Samosa' : 10,
        'Butter chicken' : -200,
        'Tandoori chicken' : None,
        'Chana masala' : 8,
        'Aloo gobi' : 12,
        'Biryani' : 0,
        'Naan' : 2
    }
    # Run the function
    indian_menu_food(indian_food_menu) # Will cause an error
except ValueError as ve:
    print(ve)
    
input("\n Press Enter to Continue...")