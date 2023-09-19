# Zachary Hoover || 9-18-23 || Guided Practice #12

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

print_header("Lists/Tuples")

my_list = [3.14159, 2.71828, 1.61803]
my_list_trunc = [math.trunc(i) for i in my_list]

print(" ", my_list_trunc)

input("\n Press Enter to Continue...")
print_header("Dictionaries")

my_dict = {'pi':3.14159, 'e':2.71828, 'phi':1.61803}
my_dict_trunc = {k:math.trunc(v) for k, v in my_dict.items()}

print(" ", my_dict_trunc)

input("\n Press Enter to Continue...")
print_header("Functions")

def my_func(x):
    return math.trunc(x)

print(" ", my_func(3.14159))

input("\n Press Enter to Continue...")
print_header("Classes")

class MyMath:
    def __init__(self, x):
        self.x = x
        
    def trunc(self):
        return math.trunc(self.x)
    
my_obj = MyMath(3.14159)
print(" ", my_obj.trunc())

input("\n Press Enter to Continue...")
print_header("Strings")

my_str = '3.14159'
my_str_trunc = str(math.trunc(float(my_str)))
print(" ", my_str_trunc)

input("\n Press Enter to Continue...")
print_header("Booleans")

my_bool = (math.trunc(3.14159) == 3)
print(" ", my_bool)

input("\n Press Enter to Continue...")
print_header("Factorial")

n =5
n = math.factorial(n)
print(" ", n)

input("\n Press Enter to Continue...")
print_header("Factorial Function")

def n_choose_k(n, k):
    return math.factorial(n) // (math.factorial(k)) * math.factorial(n-k)

n=10
k = 3
n_choose_k_10_3 = n_choose_k(n,k)
print(f"  The number of ways to choose {k} objects from {n} object is {n_choose_k_10_3}")

input("\n Press Enter to Continue...")
print_header("Loop Factorial")

result = 1
for i in range(1, n+1):
    result *= i
    
print(f"  {result}")

input("\n Press Enter to Continue...")
print_header("Recursion Factorial")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 5
result = factorial(n)
print(f"  The factorial of {n} is {result}")

input("\n Press Enter to Continue...")

