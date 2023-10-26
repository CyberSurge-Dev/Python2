# Zachary Hoover || 10-17-23 || Independent Practice #25

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

print_header("Program 1")

# Create quote variable and print it
quote = "Success is not final, failure is not fatal: It is the courage to continue that counts."
print(f"Quote:\n{quote}\n")

# Print first 5 characters
print("First 5 characters:",quote[:6]) # Succe
# Print last 5 characters
print("Last 5 characters:", quote[-5:]) # unts.
# Print every 4th character starting at 6
print("Every 4th character starting at 6:", quote[5::4]) # sstn l nflt  r ci tu.

input("\n Press Enter to Continue...")
print_header("Program 2")

# Create quote variable and print it
quote = "Be the change you wish to see in the world."
print(f"Quote:\n{quote}\n")

# Check if the word 'change' is in the quote and print a message
if 'change' in quote:
    print("'change' is present in the quote")
else:
    print("'change' is not present in the quote")
    
# Check if the word 'love' is NOT in the quote and print a message
if 'love' not in quote:
    print("'love' is not present in the quote")
else:
    print("'love' is present in the quote")

input("\n Press Enter to Continue...")
print_header("Program 3")

# Create quote variable and print it
quote = "the only way to do great work is to love what you do."
print(f"Quote:\n{quote}\n")

try:
    # This line will cause an error (individual indexs in strings are not mutable)
    quote[0] = quote[0].upper()
except TypeError as t:
    # Print error message
    print(t)
    
# Print quote after change
print(f"\nQuote after change:\n{quote}\n")  

# Print a message about why it did not work
print("""Strings are immutable objects, you can change the whole string by re-assigning it, but 
you cannot change the individual characters using the character's index. To get around this, you 
could convert the string to a list, then back into a string (using ''.join(list)) if needed.""")

input("\n Press Enter to Continue...")