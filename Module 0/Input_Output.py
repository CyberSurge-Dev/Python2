# Zachary Hoover || 8-11-23 || Python 1 Review: Input & Output

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("1. Basic Output with print()")

# print message
print("  Hello, World!")

input("\n Press Enter to Continue...")
print_header("2. Basic Input with input()")

# get name, greet user
name = input("  Enter your name: ")
print(f"  Hello, {name}!")

input("\n Press Enter to Continue...")
print_header("3. Combining Input and Output")

# get numbers
num1 = int(input("  Enter a number: "))
num2 = int(input("  Enter another number: "))

# print added numbers
print(f"\n  The sum of {str(num1)} and {str(num2)} is {str(num1 + num2)}")

input("\n Press Enter to Continue...")
print_header("4. Advanced Output Formatting")

print("  {0}, you have chosen the numbers {1} and {2}".format(name, num1, num2))

input("\n Press Enter to Continue...")

