# Zachary Hoover || 10-4-23 || Guided Practice #19

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')

print_header("IndexError")

try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception as e:
    print(e)
    print('Got an error')
    
print("\ncontinuing")

input("\n Press Enter to Continue...")
print_header("ZeroDivisionError")

try:
    x = 5
    y = x/0
    print("This won't print")
except IndexError:
    print("Got a IndexError")
except ZeroDivisionError:
    print("Got a ZeroDivisionError")
    
print("\nContinuing")

input("\n Press Enter to Continue...")
print_header("More Zero Division Errors")

try:
    # This will not print
    print(5/0)
except ZeroDivisionError:
    print("You can't devide by zero!")
    
input("\n Press Enter to Continue...")
print_header("Calculator")

print("Give me two eaqual numbers and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except Exception as e:
        print(e)
        
input("\n Press Enter to Continue...")
print_header("Else Block")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by 0!')
    else:
        print(answer)
        
input("\n Press Enter to Continue...")
