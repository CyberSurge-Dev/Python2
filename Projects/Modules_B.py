# Zachary Hoover || 9-21-23 || Independent Practice #15

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os
import math
import platform
import random

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("Math Functions")

# loop through until a valid float is entered
while True:
    try:
        # Get the input from the user
        num = float(input("  Enter a float number: "))
        break
    except:
        print("  You did not enter a float!")
        continue
    
# Print details using math and the user input
print(f"  Ceil({num}): {math.ceil(num)}")
print(f"  floor({num}): {math.floor(num)}")
print(f"  trunc({num}): {math.trunc(num)}")
print(f"  factorial({int(num)}): {math.factorial(int(num))}") # convert int for factorial
print(f"  hypot({num}): {math.hypot(num)}")
print(f"  sqrt({num}): {math.sqrt(num)}")

input("\n Press Enter to Continue...")
print_header("Random Functions")

# Create a list for items entered
items = []

# Loop through until the user is done entering items
while True:
    # get user input
    inp = input('  Enter soemthing (press Enter to exit, min 4): ')
    
    # Check for exit
    if inp == "" and len(items) > 3:
        break
    else:
        # Add input to list
        items.append(inp)
        
# Random int for prints
ranint = random.randrange(2, len(items)+1)
        
print(f"\n  Items: {items}")
print(f"\n  random.choice(items): {random.choice(items)}")
print(f"  random.sample(items, {ranint}): {random.sample(items, ranint)}")
random.shuffle(items) # shuffle items
print(f"  random.shuffle(items): {items}")

input("\n Press Enter to Continue...")
print_header("Platform Information")

# Print details using platform module
print("  Operating system:", platform.system())
print("  Processor:", platform.processor())
print("  Python version:", platform.python_version())

input("\n Press Enter to Continue...")
print_header("Explore functions")

# List functions in math
print("  dir(math): ")
print(" ", dir(math))

# List functions in platform
print("\n  dir(platform): ")
print(" ", dir(platform))

input("\n Press Enter to Continue...")