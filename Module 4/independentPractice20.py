# Zachary Hoover || 10-5-23 || Independent Practice #20

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

print_header("Addition")

# Get first number
num1 = input("\nEnter a number: ")
# get second number
num2 = input("Enter another number: ")
# use try block to check if the opperation is possible
try:
    answer = int(num1) + int(num2)
except ValueError:
    # if ValueError, print a message and restart the loop
    print("your input must be numbers!")
else:
    # Use else if succesful, break loop
    print(answer)

input("\n Press Enter to Continue...")
print_header("Addition Calculator")

while True:
    # Get first number
    num1 = input("\nEnter a number (Press Enter to quit): ")
    # Check if user wants to exit the loop
    if num1 == "":
        break
    # get second number
    num2 = input("Enter another number (Press Enter to quit): ")
    # Check if user wants to exit the loop
    if num2 == "":
        break
    # use try block to check if the opperation is possible
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        # if ValueError, print a message and restart the loop
        print("your input must be numbers!")
    else:
        # Use else if succesful, break loop
        print(answer)
        
input("\n Press Enter to Continue...")
print_header("Cats & Dogs")

try:
    # loop through files and attempt to print the contents
    for filename in ['dogs.txt', 'cats.txt']:
        # Open the file as file
        with open(path + filename) as file:
            print(f"\n{filename}:")
            # Print each line in the file
            for line in file.readlines():
                print(" ", line.rstrip())
except FileNotFoundError:
    print(f"\nFile {path + filename} does not exist.")
    
input("\n Press Enter to Continue...")
print_header("Silent Cats & Dogs")

try:
    # loop through files and attempt to print the contents
    for filename in ['dogs.txt', 'cats.txt']:
        # Open the file as file
        with open(path + filename) as file:
            print(f"\n{filename}:")
            # Print each line in the file
            for line in file.readlines():
                print(" ", line.rstrip())
except FileNotFoundError:
    # Don't print a message
    pass

input("\n Press Enter to Continue...")
print_header("Common Words")
               
# Create a list with file names
files = ['the_scarlet_letter.txt', 'dracula.txt', 'middlemarch.txt']
          
# Print message
print(f"Counts for 'the ' in {files}")      
try:
    # loop through files and attempt to print the contents
    for filename in files:
        with open(path + filename, encoding='UTF-8') as file:
            # Store contents of file in varibale
            contents = file.read()
            # Print the count
            print(f"  The file {filename} contains the phrase 'the ' approximately {contents.lower().count('the ')} times.")      
except FileNotFoundError:
    # Print message with error
    print(f"File {path + filename} does not exist.")
    
# Print message
print(f"\nCounts for 'the' in {files}")      
try:
    # loop through files and attempt to print the contents
    for filename in files:
        with open(path + filename, encoding='UTF-8') as file:
            # Store contents of file in varibale
            contents = file.read()
            # Print the count
            print(f"  The file {filename} contains the phrase 'the' approximately {contents.lower().count('the')} times.")      
except FileNotFoundError:
    # Print message with error
    print(f"File {path + filename} does not exist.")
    
input("\n Press Enter to Continue...")


