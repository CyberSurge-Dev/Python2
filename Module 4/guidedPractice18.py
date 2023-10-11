# Zachary Hoover || 10-3-23 || Guided Practice #18

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
from fileinput import filename
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

print_header("Writing to an empty file")

filename = path + 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    
print("Wrote to the empty file")

input("\n Press Enter to Continue...")
print_header("Writing to an Empty File")

with open(filename, 'w')as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating games.\n")
    
print(" Wrote to file (overides previous)")

input("\n Press Enter to Continue...")
print_header("Appending a File")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    
print("Appended lines to file")
    
input("\n Press Enter to Continue...")
print_header("Appending a File")
