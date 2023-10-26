# Zachary Hoover || 10-17-23 || Guided Practice #25

# Imports
from ctypes.wintypes import WORD
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

print_header("List Comprehensions")

my_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in my_list]
print(squared_list)

print()

even_list = [x for x in my_list if x % 2 == 0]
print(even_list)

print()

my_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in my_list for num in sublist if num % 2 == 0]
print(flat_list)

input("\n Press Enter to Continue...")
print_header("Other Comprehensions")

print("Lists")
squares = [i*i for i in range(1, 6)]
print(squares)

print("\nSets")
squares_set = {i*i for i in range(1, 6)}
print(squares_set)

print("\nDictionaries")
word = "hello"
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

print("\nStrings")
word = "hello"
vowels = ''.join([char for char in word if char in 'aeiou'])
print(vowels)

input("\n Press Enter to Continue...")
print_header("Lambdas")

multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)

print()

my_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, my_list))
print(squared_list)

input("\n Press Enter to Continue...")
print_header("Self-Defined")

def apply_opperation(opperation, x, y):
    return opperation(x, y)

result = apply_opperation(lambda x, y: x + y, 3, 4)
print(result)

input("\n Press Enter to Continue...")
print_header("map() and filter()")

def square(x):
    return x ** 2

my_list = [1, 2, 3, 4, 5]
squared_list = list(map(square, my_list))
print(squared_list)

print()

def is_even(x):
    return x % 2 == 0

my_list = [1, 2, 3, 4, 5]
even_list = list(filter(is_even, my_list))
print(even_list)

input("\n Press Enter to Continue...")
print_header("Filter Examples")

filtered_numbers = list(filter(lambda x: x % 2 != 0, range(1, 11)))
print(filtered_numbers)

words = ["apple", "banana", "orange0, 'kiwi", "peach"]
filtered_words = list(filter(lambda x: len(x) < 5, words))
print(filtered_words)

print()

numbers = range(10, 101, 10)
filtered_numbers = tuple(filter(lambda x: x > 50, numbers))
print(filtered_numbers)

print()

numbers = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
filtered_numbers = dict(filter(lambda x: x[1] % 2 == 0, numbers.items()))
print(filtered_numbers)

input("\n Press Enter to Continue...")
print_header("Map Examples")

strings = ['apple', 'banana', 'cherry']
lengths = map(len, strings)
print(list(lengths)) 

print()

# Define the function to square a number
def square(x):
    return x ** 2

# Define the list of numbers to square
numbers = [1, 2, 3, 4, 5]

# use map() to apply square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list and prints the result
print(list(squared_numbers))

print()

# Define the list of strings
strings = ['apple', 'banana', 'cherry']
# Use map() to apply the upper() method to each in the list
uppercase_strings = map(str.upper, strings)
# Convert the map object to a list and print the result
print(list(uppercase_strings))

print()

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# use map() to apply a lambda function to each number in the list
result = map(lambda x: x * 2 +1, numbers)

# Convert the map object to a list and print the result
print(list(result))

input("\n Press Enter to Continue...")