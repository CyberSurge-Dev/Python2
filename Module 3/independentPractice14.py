# Zachary Hoover || 9-20-23 || Independent Practice #14

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import math
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("The Vet")

class Coordinates():
    """Simple class to calculate coords between 2 points"""
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        
    def calculate_distance(self):
        """Returns the distance between the two Coordinates"""
        return math.hypot(self.pos2[0] - self.pos1[0], self.pos2[1] - self.pos1[1])

# Filter user input to make sure that the correct numbers are processed
pos1 = [int(i.strip().replace(')', '').replace('(', '')) for i in input("  Enter the first pos (x, y): ").split(',')] # Set first coord
pos2 = [int(i.strip().replace(')', '').replace('(', '')) for i in input("  Enter the second pos (x, y): ").split(',')] # Set second coord

# Create an instance of the Coordinates class
coords = Coordinates(pos1, pos2)

# Print a message abput the distance
print(f"  The distance between he points is {coords.calculate_distance():.2f}")
    
input("\n Press Enter to Continue...")
print_header("Cat Tower")

while True:
    try:
        # Get height from user
        height = int(input("  Enter the height of the tower: "))
        
        # Check if height is above 6
        if height < 6:
            raise Exception("The height cannot be below 6 feet.")
        
        # Get base y and z
        y = int(input("  Enter the length of the base: "))
        z = int(input("  Enter the width of the base: "))
        
        # get length of diagonal (hypot) on the base square
        base_diag_half = math.hypot(y, z)/2
        
        # Get the length of the diagonal usind the height and half of the distance accross the base
        diagonal = math.hypot(base_diag_half, height)
        
        # Print the result
        print(f"  The length of the diagonal of the entered cat tower is: {diagonal:.2f}")
        
        break
    
    except Exception as e:
        print("\n ", e)
        continue

input("\n Press Enter to Continue...")
print_header("Age Gap")

# get the age of the first cat
cat1_age = int(input("  Enter the age of your first cat (yrs): "))
cat2_age = int(input("  Enter the age of your second cat (yrs): "))

# Convert the age of the cats to months
cat1_age *= 12
cat2_age *= 12

# Prints thee result as the absolute value of the difference between the cat's ages in months
print(f"  The age difference between your cats in months is {abs(cat1_age-cat2_age)}")

input("\n Press Enter to Continue...")