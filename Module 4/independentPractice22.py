# Zachary Hoover || 10-11-23 || Independent Practice #22

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

print_header("Mario Kart")

def check_kart(top_speed, acceleration, weight):
    """Checks the carious attributes of a kart with stats passed in."""
    try:
        # Check conditions, if false raise assertion error
        assert type(top_speed) == int and top_speed <= 200 and top_speed >= 0, "Invalid top speed"
        assert type(acceleration) == float and acceleration <= 10 and acceleration >= 0, "Invalid acceleration"
        assert type(weight) == float and weight <= 500 and weight >= 0, "Invalid weight"
    # Check for any assertion errors
    except AssertionError as a:
        # Raise an exception with the assertion
        raise ValueError(f"Your kart is invalid: {a}")
    else:
        # Return a message if kart has no issues
        return "Kart is elgible for the race"
    
# Loop through until user inputs valid numbers
while True:
    try:
        # Get input from the user, convert them to correct type
        ts = int(input("Enter the top speed of your kart (0-200): "))
        a = float(input("Enter the acceleration of your kart (0-10): "))
        w = float(input("Enter the eight of your kart (0-500): "))
    # Catch any ValueErrors from details entered
    except ValueError as ve:
        print(ve)
        continue
    else:
        break
        
# Check the kart
try:
    # Print the result of checking the kart
    print(check_kart(ts, a, w))
except ValueError as va:
    # Print any ValueErrors
    print(va)
    
input("\n Press Enter to Continue...")
print_header("Doctor Mario")

def check_capsule(color, direction):
    """Checks if the color and direction passed in are valid."""
    try:
        # Check if color and direction are valid, raise AssertionError if false
        assert color.lower() in ['r', 'b', 'y'], "Color not valid"
        assert direction.lower() in ['u', 'd'], "Direction not valid"
    except AssertionError as a:
        # Raise a ValueError for any AssertionErrors caught
        raise ValueError(f"Invalid input: {a}")
    else:
        # If succesful, return a string.
        return "Capsule can eliminate virus"
    
# Get user input
color = input("Enter a color ('r', 'b', 'y'): ")
direction = input("Enter direction ('u', 'd'): ")
        
# Check the kart
try:
    # Print the result of checking the capsule
    print(check_capsule(color, direction))
except ValueError as va:
    # Print any ValueErrors
    print(va)
    
input("\n Press Enter to Continue...")
print_header("Doctor Mario")

def check_energy(current_energy, weapon_energy):
    """Check the characters current energy and weapon's current energy, raises a ValueError if not valid."""
    try:
        # Check the current_energy and weapon energy, check if there is enough current energy to fire weapon
        assert current_energy > 0, "Samus' energy cannot be negative"
        # Check id weapon energy is valid, and if there is enough energy to fire weapon
        assert weapon_energy > 0, "Samus' weapon energy cannot be negative"
        assert weapon_energy <= current_energy, "Samus' does not have enough energy to fire her weapon"
    except AssertionError as a:
        raise ValueError(f"Invalid input: {a}")
    else:
        # If valid, return a message
        return "Samus can fire her weapon"
    
# Loop through until user inputs valid numbers
while True:
    try:
        ce = int(input("Enter Samus' current energy: "))
        we = int(input("Enter Samus' weapon energy: "))
        # Catch any ValueErrors from details entered
    except ValueError as ve:
        print(ve)
        continue
    else:
        break
        
# Check the kart
try:
    # Print the result of checking the energy
    print(check_energy(ce, we))
except ValueError as va:
    # Print any ValueErrors
    print(va)
    
input("\n Press Enter to Continue...")