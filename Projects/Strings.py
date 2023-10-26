# Zachary Hoover || 10-18-23 || Mini Project: Strings

# Imports
import math
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

print_header("Task 1")

# Create an empty list to store numbers entered by the user
nums = []
# Loop through and allow user to add numbers
while True:
    try:
        # Get the user input
        num = input("Enter integers (press Enter to quit): ")
        
        if num == '':
            # Break if the input is empty
            break
        else: 
            # Try to convert the input to an integer and add it to the list
            nums.append(int(num))
    except ValueError:
        # Print an error if the input is not valid
        print("Your input needs to be a integer.")
        
# Clear the screen
print_header("Task 1")

# Print the list created
print(f"List created: {nums}")
# Print sorted list
print(f"Sorted list: {sorted(nums)}")

input("\n Press Enter to Continue...")
print_header("Task 2")

# Create an empty list to store the users entered strings
strs = []
while True:
    # Allow the user to enter a string
    string = input("Enter a string (press Enter to quit): ")
    if string == "":
        # Check if string is empty and quit
        break
    else:
        # Add the string to the list of strings
        strs.append(string)
        
# Clear the screen
print_header("Task 2")   

def word_sorted(lst):
    """Sorts a list, and ignores capitilization and numbers"""     
    sorted_list = sorted([x.lower() for x in strs])

# Print the list created
print(f"List created: {strs}")
# Print sorted list, making all words lowercase to have propper sorting (numbers will automatically go to front of list)
print(f"Sorted list: {sorted([x.lower() for x in strs])}")

input("\n Press Enter to Continue...")
print_header("Task 3")

# Loop through until a valid response is entered
while True:
    try:
        inp = input("Enter a string and a number seperated by commas (str, num): ")
        
        if inp.count(',') > 1:
            # Check if the value entered contains more than one comma
            raise ValueError
        # Split the input into a string and integer
        inp = [inp.split(', ')[0], int(inp.split(', ')[1])]
        
        # Create the string
        new_str = inp[0] * inp[1]
        if len(new_str) > 10:
            # Check if the string is over 10, print first 3 and last 3
            print(new_str[:3] + new_str[-3:])
        else:
            # If the string is under 10 characters, print in all upercase
            print(new_str.upper())

        break
    except ValueError as e:
        print("You must enter a string with no commas in the following form: str, int\n")
        continue
    
input("\n Press Enter to Continue...")
print_header("Task 4")

# Loop through and allow user to add numbers
while True:
    try:
        # Get the user input
        num = float(input("Enter a number: "))

        # Print a floored result of the square root of the number entered, using string formating to cut off decimals
        print("Rounded square root of number entered: {:.0f}.".format(math.sqrt(num)))

        break
    except ValueError as ve:
        # Print an error if the input is not valid
        print("Your input needs to be a number.")
        print(ve)

input("\n Press Enter to Continue...")