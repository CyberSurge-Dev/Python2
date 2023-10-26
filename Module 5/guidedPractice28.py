# Zachary Hoover || 10-25-23 || Guided Practice #28

# Imports
import os
import sys

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

print_header("I/O Introduction")

try:
    with open("alice.txt", "rb") as f:
        data = f.read()
except FileNotFoundError as fn:
    print(fn)    
    
print()

try:
    with open("image.png", "rb") as f:
        data = f.read()
except FileNotFoundError as fn:
    print(fn)    
    
input("\n Press Enter to Continue...")
print_header("Predefined Streams")

name = input("Enter your name: ")
print("Hello, " + name + "!")

print()

print("Hello, world!")

print()

print("Error: File no found", file = sys.stderr)

input("\n Press Enter to Continue...")
print_header("Handles vs Streams")

try:
    file_handle = open("alice.txt", "r", encoding="utf-8")
    file_contents = file_handle.read()
    file_handle.close()
except FileNotFoundError as fn:
    print(fn)

input("\n Press Enter to Continue...")

