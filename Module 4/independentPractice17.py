# Zachary Hoover || 10-2-23 || Independent Practice #17

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

print_header("Learning Python")

# Store the filename in a variable
filename = path + "learning_python.txt"

print("Print entire file:")

# Print the entire file
with open(filename, 'r') as file:
    print(file.read())
    
print("\nPrint file by looping over file")

# Print looping over the file
with open(filename, 'r') as file:
    for line in file:
        print(line.rstrip())
        
print("\nAdd lines to list and print:")
# create a list for the lines
lines = []
with open(filename, 'r') as file:
    for line in file.readlines():
        lines.append(line.rstrip())
        
# Print lines using a for loop
for line in lines:
    print(line)
    
input("\n Press Enter to Continue...")
print_header("Learning C (Replace 'Python' With 'C')")

# Print entire file, replacing pythin with another programming language
with open(filename, 'r') as file:
    print(file.read().replace('Python', 'C'))

input("\n Press Enter to Continue...")