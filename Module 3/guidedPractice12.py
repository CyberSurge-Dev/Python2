# Zachary Hoover || 9-18-23 || Guided Practice #12

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Code to clear the screen before running
import os
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("Standard Library")

from random import randint

x = randint(1, 6)

from random import choice 

players = ['Charles', 'Martina', 'Michael', 'Florence', 'Eli']
first_up = choice(players)
print("  Your up first,", first_up)

input("\n Press Enter to Continue...")
print_header("ceil() Example")

import math

print("  Ceil 3.2:", math.ceil(3.2))
print("  Ceil 3.7:", math.ceil(3.7))
print("  Ceil 4:", math.ceil(4))

input("\n Press Enter to Continue...")
print_header("floor() Example")

print("  Floor 3.2:", math.floor(3.2))
print("  Floor 3.7:", math.floor(3.7))
print("  Floor 4:", math.floor(4))

input("\n Press Enter to Continue...")
print_header("tunc() Example")

print("  Trunc 3.2:", math.trunc(3.2))
print("  Trunc 3.7:", math.trunc(3.7))
print("  Trunc 4:", math.trunc(4))

input("\n Press Enter to Continue...")
print_header("hypot() Example")

print("  Hypot 3, 4:", math.hypot(3, 4)) # 5.0
print("  Hypot 5, 12:", math.hypot(5, 12)) # 13.0

input("\n Press Enter to Continue...")
print_header("sqrt() Example")

print("  Sqrt 9:", math.sqrt(9)) # 3
print("  Sqrt 16:", math.sqrt(16)) # 4

input("\n Press Enter to Continue...")
print_header("ceil() With Lists, Tuples, and Dictionaries")

my_list = [2.5, 3.7, 4.2, 5.9]
my_tuple = (1.3, 2.7, 3.1, 4.5)

# use ceil() with lists
for number in my_list:
    print(f"  Ceil {number}:",math.ceil(number))

print() # Spacer

# use ceil() with tuples    
for number in my_tuple:
    print(f"  Ceil {number}:",math.ceil(number))
    
print() # Spacer
    
my_dict = {'a':2.5, 'b':3.2, 'c':4.2, 'd':5.9}

# using ceil() with dictionaries
for key in my_dict.keys():
    print(f"  Ceil {my_dict[key]}:", math.ceil(my_dict[key]))
    
print() # Spacer
    
def calculate_total_cost(cost_per_unit, quantity):
    return math.ceil(cost_per_unit * quantity)

print(" ", calculate_total_cost(2.5, 3))

input("\n Press Enter to Continue...")
print_header("ceil() With Classes")

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return(2* (self.width + self.height))
    
    def calculate_area(self):
        return (self.width * self.height)
    
    def calculate_required_paint(self, paint_coverage):
        total_area = self.calculate_area()
        
        return math.ceil(total_area / paint_coverage)
    
rect = Rectangle(5, 3)

print("  Required paint for rect:", rect.calculate_required_paint(10)) # output 2

input("\n Press Enter to Continue...")
print_header("ceil() With strings")

my_string = "Python is a slow language"

# use ceil() with strings
num_of_chars = len(my_string)
num_of_pages = math.ceil(num_of_chars / 20)

print("  Number of pages required:", num_of_pages)

input("\n Press Enter to Continue...")
print_header("ceil() With If and Loops")

for i in range(0, 10):
    if math.ceil(i/2) >= 3:
        print(" ", i)
        
input("\n Press Enter to Continue...")
print_header("floor() Examples")

numbers = [3.14, 5.9, 6.8, 7.2, 10.1]
floors = [math.floor(i) for i in numbers] # Use list comprehension to creat a list of floored numbers
print("  Floored numbers:", floors)

print() # Spacer

prices = {'apple':2.99, 'banana':1.49, 'orange':1}
floor_prices = {k: math.floor(v) for k, v in prices.items()} # Create dictionary using dictionary comprehension
print("  Floored dictionary:", floor_prices)

print() # Spacer

def calculate_total_cost(cost_per_unit, quantity):
    return math.floor(cost_per_unit * quantity)

cost = calculate_total_cost(2.99, 3)
print(" ", cost)

print() # Spacer

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)
    
    def rounded_area(self):
        return math.floor(self.area())
    
rect = Rectangle(3.5, 2.25)
print(" ", rect.area())
print(" ", rect.rounded_area())

print() # Spacer

string = "hello, world!"

num_chars = len(string)

num_chunks = math.floor(num_chars / 5)

chunks = [string[i:i+5] for i in range (0, num_chars, 5)]

print(" ", num_chars)
print(" ", num_chunks)
print(" ", chunks)

input("\n Press Enter to Continue...")