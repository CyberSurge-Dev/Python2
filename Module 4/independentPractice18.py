# Zachary Hoover || 10-2-23 || Independent Practice #17

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os
from urllib import response

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

print_header("Guest")

# Store the path of the file to be read
filename = path + 'guest.txt'

# Get the users name
username = input("Enter your name: ")

# Write the users name to the guest.txt file
with open(filename, 'w') as file:
    file.write(username)

input("\n Press Enter to Continue...")
print_header("Guest Book")

filename = path + 'guest_book.txt'

# Create an empty list to store peoples names
people = []
while True:
    # Ask the user for there name and stoe it in a variable
    username = input("Enter your name (Press enter to quit): ")
    # Check if the user wants to exit the loop
    if (username == ""):
        break
    # Append the users name to the people list (\n for new line)
    people.append(username+'\n')
    # Print a greeting for the user.
    print(f"\nHello {username}!\n")
    
# Add the contents of people in a file called guest_book.txt
with open(filename, 'a') as file:
    file.writelines(people)
    
input("\n Press Enter to Continue...")
print_header("Programming Poll")

filename = path + 'programming_poll.txt'

while True:
    # Ask the user for there response and stoe it in a variable
    print("What do you like about programming?")
    response = input("Enter response (Press enter to quit): ")
    # Check if the user wants to exit the loop
    if (response == ""):
        break
    # Append the users name to the programming_poll file
    with open(filename, 'a') as file:
        # add \n for new line
        file.write(response+'\n') 
    # Print a greeting for the user.
    print(f"\nThank you for the response!\n")

input("\n Press Enter to Continue...")
    
    
