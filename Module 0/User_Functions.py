# Zachary Hoover || 8-11-23 || Python 1 Review: User Functions

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("1. Basic Function Creation and Call")

def display_message():
    """Displays a message"""
    print("  Hello from inside the function!")

display_message()

input("\n Press Enter to Continue...")
print_header("2. Parameters and Arguments")


def greet_user(name):
    """Greets a user"""
    print(f"  Hello, {name}!")
    return

n = input("  Enter your name: ")
greet_user(n)

input("\n Press Enter to Continue...")
print_header("3. Return Values")

def add_numbers(num1, num2):
    """Returns the sum of 2 numbers."""
    return num1 + num2

result = add_numbers(21, 36)
print("  The sum of 21 and 36 is", result)

input("\n Press Enter to Continue...")
print_header("4. Positional Arguments")

def describe_pet(animal_type, pet_name):
    """Prints a sentence about the pet"""
    print(f"  Your {animal_type} is named {pet_name}")

describe_pet("dog", "Whiskers")

input("\n Press Enter to Continue...")
print_header("5. Keyword Arguments")

describe_pet(pet_name="Whiskers", animal_type='cat')

input("\n Press Enter to Continue...")
print_header("5. Keyword Arguments")

describe_pet("bird", pet_name='Tweety')

input("\n Press Enter to Continue...")


