# Zachary Hoover || 8-14-23 || Python 1 Review: Loops

import time

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Exercise 1: Write a Python function sum_of_n(n) that returns the sum of the first n natural (positive) numbers using a for loop.")

def sum_of_n(n):
    """Returns first positive number in list"""
    out = 0
    for num in n:
        if num > 0:
            out += num
    return out

    return out

ls = []
while True:
    inp = input("  Enter a number (Enter 'quit' to exit): ")
    if inp.lower() == "quit":
        break
    else:
        ls.append(float(inp))

print("\n  List:", ls)
print("  Sum of all positives in the list:", sum_of_n(ls))

input("\n Press Enter to Continue...")
print_header("Exercise 2: Write a Python function countdown(n) that prints a countdown from n to 1.")

def countdown(num):
    """Counts down num number of seconds"""
    ls = reversed(range(0, num+1))
    for n in ls:   
        print(f"  {int(n)}...")
        time.sleep(1)

tm = int(input("  How many seconds would you like to wait?: "))
countdown(tm)

input("\n Press Enter to Continue...")
print_header("Exercise 3: Combining for Loops with Functions:")

def factorial(num):
    """Returns factorical of number"""
    out = num
    for n in range(1, num):
        out *= (num-n)

    return out

num = int(input("  Enter a number: "))
print(f"  The factorial of {int(num)} is", factorial(num))

input("\n Press Enter to Continue...")
print_header("Exercise 4: Combining while Loops with Functions")

def find_power_of_two(num):
    """Returns the power of 2 greater than a given number n. Use a while loop to accomplish this."""



        




