# Zachary Hoover || 10-2-23 || Guided Practice #17

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# imports
from importlib.resources import contents
import os
# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

# variable to get folder location
path = __file__[:-19]

print_header("Reading a File")

file = open(f"{path}\\ccdata.txt") # Unused code

with open (f"{path}\\ccdata.txt", 'r') as file_object:
    lines = file_object.read()
    
print(lines) # Print lines to console

file.close() # close file (unused)

input("\n Press Enter to Continue...")
print_header("Iterating over lines in a file")

file = open(f"{path}\\ccdata.txt")

for aline in file:
    values = aline.split()
    print('in', values[0], 'the average temp was', values[1], '*C and CO2 emmisions were', values[2], 'gigatons.')
    
file.close()

input("\n Press Enter to Continue...")
print_header("Reading from a File")

with open(f"{path}\\pi_digits.txt") as  file_object:
    contents = file_object.read()
    
print(contents) # Print file data
print(contents.rstrip())

input("\n Press Enter to Continue...")
print_header("Line by Line")

filename = f"{path}\\pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)
        
input("\n Press Enter to Continue...")
print_header("Line by Line")

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

input("\n Press Enter to Continue...")
print_header("making a List")

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())

input("\n Press Enter to Continue...")
print_header("File's Content")

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))

input("\n Press Enter to Continue...")
print_header("Milions")

filename = f'{path}\\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))

input("\n Press Enter to Continue...")
print_header("Birthday")

birthday = input("Enter your birthday (mmddyy): ")

if birthday in pi_string:
    print("\nYour birthday is in the first million digits of pi!")
else:
    print("Your birthday is not in the first million digits of pi.")
    
input("\n Press Enter to Continue...")