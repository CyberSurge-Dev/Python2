# Zachary Hoover || 8-11-23 || Python 1 Review: Python Basics

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("1. Data Types & Variables")

# Create variables
my_int = 10
my_str = "Python"
my_float = 3.14

# Print types
print(" ", my_int, type(my_int))
print(" ", my_str, type(my_str))
print(" ", my_float, type(my_float))

input("\n Press Enter to Continue...")

print_header("2. Operators")

# Set variables
a = 5
b = 3

print("  a =", a)
print("  b =", b)

# Proform operations and print
print("\n  a + b:", a + b)
print("  a - b:", a - b)
print("  a * b:", a * b)
print("  a / b:", a / b)
print("  a // b:", a // b)
print("  a % b:", a % b)
print("  a ** b:", a ** b)

input("\n Press Enter to Continue...")

print_header("3. Booleans and Comparison Operators")

print("  a =", a)
print("  b =", b)

print("\n  a == b:", a == b)
print("  a != b:", a != b)
print("  a > b:", a > b)
print("  a < b:", a < b)

input("\n Press Enter to Continue...")


print_header("3. Booleans and Comparison Operators")

def greet(name):
    """Greets the person whose name is passed in"""
    print(f"  Hello, {name}!")

n = input("  What is your name?: ")
greet(n)

input("\n Press Enter to Continue...")

