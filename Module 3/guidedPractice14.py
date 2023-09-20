# Zachary Hoover || 9-20-23 || Guided Practice #14

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# imports
import math
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("hypot() Examples")

a = 3
b = 4
c = math.hypot(a, b)

print(" ", c)

print() # Spacer

is_right_triangle = (a**2 + b**2 == math.hypot(a, b) ** 2)

if is_right_triangle:
    print("  This is a right triangle!")
else:
    "  This is not a right triangle."
    
print() # Spacer

player_name = "Steve"
a = 3
b = 4
c = math.hypot(a, b)

print(f"  Hello {player_name}! The length of the hypotenuse is {c}.")

print() # Spacer

for i in range(1, 11):
    print(f"  The length of the hypotenuse for sides {i} and {i+1} is {math.hypot(i, i+1)}")

print() # Spacer

def distance(pos1, pos2):
    dx = pos2[0]- pos1[0]
    dy = pos2[1] - pos1[1]
    return math.hypot(dx, dy)

p1 = (0, 0)
p2 = (3, 4)
print(f"  The distance between {p1} and {p2} is {distance(p1, p2)}")

input("\n Press Enter to Continue...")
print_header("sqrt() Examples")

def hypotenuse(a, b):
    """Calculate the length of the hypotenuse of a right triangle"""
    return math.sqrt(a**2 + b**2)

a = 3
b = 4
c = hypotenuse(a, b)
print(f"  The hypotenuse of a triangle with sides {a} and {b} is {c:.2f}")

class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return 2 * self.radius
    
    def surface_area(self):
        return 4 * math.pi * self.radius**2
    
    def volume(self):
        return (4/3) * math.pi * self.radius**3
    
r = 5
circle = Circle(5)

print(f"  The area of a circle with radius 5 is: {circle.area()}")
print(f"  The circumference of a circle with radius 5 is: {circle.circumference()}")
print(f"  The diameter of a circle with radius 5 is: {circle.diameter()}")
print(f"  The surface area of a circle with radius 5 is: {circle.surface_area()}")
print(f"  The volume of a circle with radius 5 is: {circle.volume()}")

print()

x = 9
if math.sqrt(x) % 1 == 0:
    print(f"  {x} is a perfect square")
else:
    print(f"  {x} is not a perfect square")
    
print()

for i in range(1, 11):
    print(f"  The square root of {i} is {math.sqrt(i):.2f}")
    
print()

numbers = [1, 4, 9, 16, 25]
square_roots = [math.sqrt(n) for n in numbers]
print(f"  {square_roots}")

input("\n Press Enter to Continue...")