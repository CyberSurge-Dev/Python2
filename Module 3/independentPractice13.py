# Zachary Hoover || 9-19-23 || Independent Practice #13

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import math

print_header("Program 1")

# Loop until a valid integer is entered
while True:
    try:
        # Get user input
        num = int(input("  Enter a number: "))
        
        # Print the factorial of the number
        print(f"\n  Factorial of {num}: {math.factorial(num)}")
        
        break
    except:
        # Print message and return back to loop
        print(f"  Number entered is not a valid integer")
        continue
        


input("\n Press Enter to Continue...")
print_header("Program 2")

class HelloKitty():
    """Simple class with an arbitrary name"""
    def __init__(self, age ):
        """Initialize the HelloKitty class"""
        self.age = age
        
    def print_age(self):
        """Prints the truncated age"""
        
        print(f"  Age: {math.trunc(self.age)}")
        
# Initialize instance of HelloKitty class with float
hk = HelloKitty(3.141592653589793)

# Print the age
hk.print_age()

input("\n Press Enter to Continue...")
print_header("Program 3")

# loop through until a valid float is entered
while True:
    try:
        # Get the input from the user
        num = float(input("  Enter a float number: "))
        break
    except:
        print("  You did not enter a float!")
        continue
    
print() # spacer
trunc_num = math.trunc(num)
# Print the truncated number
print(f"  Truncated number: {trunc_num}")
# Check if the truncated number is even or odd and print a message
if (trunc_num % 2 == 0):
    # Print message
    print("  The truncated number is even")
else:
    # Print message
    print("  The truncated number is odd")
    
input("\n Press Enter to Continue...")
print_header("Program 4")

# Loop until a valid integer is entered
while True:
    try:
        # Get user input
        num = int(input("  Enter a positive number: "))
        
        # Check if the number is below 0
        if num < 0:
            # Raise an exception about the numbr
            raise Exception("The number entered cannot be negative")
        
        break
    except Exception as e:
        # Catch and print the exception     
        print(" ", e)
        
        # Return the user to beginning to enter a new number
        continue
        
# Print the factorial of the number
print(f"\n  Factorial of {num}: {math.factorial(num)}")

input("\n Press Enter to Continue...")
    
