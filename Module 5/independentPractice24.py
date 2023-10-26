# Zachary Hoover || 10-16-23 || Independent Practice #24

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

print_header(".isxxxx()")

# Test string for only alphnumeric characters
str = "May the force be with you"
print(f"is '{str}' only alphanumeric? {str.isalnum()}")

# Test string for only alphabetical characters
str = "Live long and prosper"
print(f"is '{str}' only alpha? {str.isalpha()}")

# Test string for only digit characters
str = "I'll be back"
print(f"is '{str}' only digits? {str.isnumeric()}")

# Test string for only whitespace characters
str = "Winter is coming"
print(f"is '{str}' only whitespace? {str.isspace()}")

# Test string for only titlecase characters
str = "Just Do It"
print(f"is '{str}' only titlecase? {str.istitle()}")

# Test string for only uppercase characters
str = "Houston, we have a problem"
print(f"is '{str}' uppercase? {str.isupper()}")

input("\n Press Enter to Continue...")
print_header("ord() & chr()")

def ascii_value(value):
    """Resturns the ASCII value corrosponding with the character passed in"""
    return ord(value)

# get string from user
str = input("Enter a character: ")
print(f"ASCII codes for {str[0]} is:\n{ascii_value(str[0])}")

def unicode_character(value):
    """Returns the unicode character corrosponding the integer entered"""
    return chr(value)

# Allow the user to enter values until an integer is entered
while True:
    try:
        # Get user input
        num = int(input("\nEnter a number: "))
    except ValueError:
        # Print a message for exception
        print("Please enter a number. \n")
    else:
        break
# Print a message with the character corrosponding with number entered by user.
print(f"The unicode character corrosponding with {num} is {unicode_character(num)}")
    
input("\n Press Enter to Continue...")
print_header("Strings & Lists")
    
def string_to_ascii(value):
    """Resturns a list of ASCII values corrosponding with the characters passed in"""
    return [ord(x) for x in value]

# get string from user
str = input("Enter a string: ")
print(f"ASCII codes for given characters:\n{string_to_ascii(str)}")

def ascii_to_string(value):
    """Returns the string formed by the passed in ascii characters"""
    return str([chr(i) for i in value])

print(f"Values entered back into a string: {ascii_to_string(string_to_ascii(str))}")

input("\n Press Enter to Continue...")