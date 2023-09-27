# Zachary Hoover || 9-26-23 || Guided Practice #16

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# imports
import os
import platform
import math
import sys

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("Platform Module")

# Print details using platform module
print("  System:", platform.system())
print("  Processor:", platform.processor())
print("  Node:", platform.node())
print("  Release:", platform.release())
print("  Machine:", platform.machine())
print("  Version:", platform.version())
print("  Architecture:", platform.architecture())
print("  Python version:", platform.python_version())
print("  Python implementation:", platform.python_implementation())

input("\n Press Enter to Continue...")
print_header("dir() Function")

print(" ", dir(math))

input("\n Press Enter to Continue...")
print_header("Object's Attributes")

string = "hello sushi"
print(dir(string))

input("\n Press Enter to Continue...")
print_header("Current Scope")

def my_function():
    x = 5
    print(" ", dir())
    
my_function()

input("\n Press Enter to Continue...")
print_header("Sys.path Variable")

print(" ", sys.path)

input("\n Press Enter to Continue...")
print_header("Add/Remove Directories")

sys.path.append('/path/to/my/module')
print(" ", sys.path)

input("\n Press Enter to Continue...")
print_header("Version Tuple")

version_tuple = sys.version_info
print(" ", version_tuple)
print("  Python Version", '.'.join(map(str, version_tuple)))

input("\n Press Enter to Continue...")
print_header("Directory")

from my_package.my_module import my_function
my_function()

# Imports 
from my_package import module1
from my_package.subpackage import module3
from my_package.subpackage.module4 import some_function

some_function()

# Will not display anything because module was initialized prior to import
from my_package import my_module

input("\n Press Enter to Continue...")
    
    

