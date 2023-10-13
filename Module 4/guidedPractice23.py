# Zachary Hoover || 10-12-23 || Guided Practice #23

# Imports
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

print_header("Self-Defined Exceptions")

class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("Something went wrong.")
except MyCustomException as e:
    print("Caught an instance of MyCustomException:", e)

input("\n Press Enter to Continue...")
print_header("Example 1")

class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        self.message = f"Error: {number} is a negative number"
        super().__init__(self.message)
        
x = input("Enter a number: ")
x = int(x)

if x < 0: raise NegativeNumberError(x)

input("\n Press Enter to Continue...")
print_header("Example 2")

class FileNotFoundError(Exception):
    def __init__(self, filename):
        self.filename = filename
        self.message = f"Error: {filename} not found."
        super().__init__(self.message)
        
try:
    with open("alice.txt", "r") as f:
        print("File opened successfully")
# Overidden by built in exception
except FileNotFoundError as e:
    print(e)
    
input("\n Press Enter to Continue...")



    