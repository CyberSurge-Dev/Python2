# Zachary Hoover || 10-11-23 || Guided Practice #22

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

print_header("Assert Exception")

def divide(a, b):
    assert b != 0, "Division by zero"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as a:
    print(a)
    
input("\n Press Enter to Continue...")
print_header("Loops")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    try:
        assert num > 0, "Invalid number"
        print(num)
    except AssertionError as a:
        print(a)
        
input("\n Press Enter to Continue...")
print_header("Functions")
        
def calculate_total(price, quantity):
    assert price >= 0 and quantity >= 0, "Invalid input"
    return price * quantity

try:
    print(calculate_total(-10, 5))
except AssertionError as a:
    print(a)
    
input("\n Press Enter to Continue...")
print_header("Tupkes")

person = ("John", "Doe", 30)
try:
    assert len(person) == 3, "Invalid tuple"
except AssertionError as a:
    print(a)
    
input("\n Press Enter to Continue...")
print_header("Lists")

items = ["apple", "banana", "Orange"]
try:
    assert "pear" in items, "Item not found"
except AssertionError as a:
    print(a)
    
input("\n Press Enter to Continue...")
print_header("Dictionaries")
    
person = {"name" : "John", "age" : 30}
try:
    assert "email" in person, "Email not found"
except AssertionError as a:
    print(a)
    
input("\n Press Enter to Continue...")
print_header("Classes")

class Rectangle:
    def __init__(self, width, height):
        assert width > 0 and height > 0, "Invalid input"
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
try:
    rect = Rectangle(-10, 5)
    print(rect.area())
except AssertionError as a:
    print(a)
    
input("\n Press Enter to Continue...")
print_header("If Statements")

try:
    num = int(input("Please enter a number between 0-10: "))
except ValueError:
    num = 0
    
if num > 0:
    assert num < 10, "Number out of range"
    print("Number is valid")
else:
    print("Number is invalid")
    
input("\n Press Enter to Continue...")