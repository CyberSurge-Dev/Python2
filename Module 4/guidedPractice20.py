# Zachary Hoover || 10-5-23 || Guided Practice #20

# Imports
from importlib.resources import contents
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

print_header("Alicein Wonderland")

filename = path + 'alice.txt'

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

input("\n Press Enter to Continue...")
print_header("Analyzing Text")

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate umber of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about about {num_words} words.")
    
input("\n Press Enter to Continue...")
print_header("Working with Multiple Files")

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about about {num_words} words.")
        
# Print wordcount of several files.
for filename in ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']:
    count_words(path + filename)

input("\n Press Enter to Continue...")
print_header("Failing Silently")

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about about {num_words} words.")

# Print wordcount of several files.
for filename in ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']:
    count_words(path + filename)
    
input("\n Press Enter to Continue...")