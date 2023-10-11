# Zachary Hoover || 10-4-23 || Independent Practice #19

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os

# Print instructions
print("Enter two integer numbers to be added.")

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')

print_header("Task 1")

# Print instructions
print("Enter two integer numbers to be divided.")

# Loop through until the user has a successful opperation
while True:
    # Get first number
    num1 = input("\nEnter a number: ")
    # get second number
    num2 = input("\nEnter a number: ")
    # use try block to check if the opperation is possible
    try:
        answer = int(num1) / int(num2)
    except ZeroDivisionError:
        # if ZeroDivisionError, print a message and restart the loop
        print("You cannot divide by zero!")
    except ValueError:
        # if ValueError, print a message and restart the loop
        print("your input must be numbers!")
    else:
        # Use else if succesful, break loop
        print(answer)
        break # exit loop

input("\n Press Enter to Continue...")
print_header("Task 2")

# Create list of characters
characters = ['Mario', 'Link', 'Sonic', 'Pikachu', 'Kratos']
# Print list
print("Characters:", characters)

# Loop through and allow the user to get several items from the list
while True:
    # Get index from user
    index = input("\nEnter the index of character: ")
    # Use try block to test if the character is retrievable
    try:
        print('Character Selected:', characters[int(index)])
        break
    except IndexError:
        # Catch index error and print message
        print(f"The input is not in range. Your input must be a number between 0-{len(characters)-1}")
    except ValueError:
         # Catch value error and print message
        print(f"Your input must be a number between 0-{len(characters)-1}")

input("\n Press Enter to Continue...")