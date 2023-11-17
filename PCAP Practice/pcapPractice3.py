# Zachary Hoover || 11-16-23 || PCAP Practice #3

# Imports
import os
import math

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

def print_header(title):
    """Prints header with title."""
    # clear()
    print("\n ------+ " + title + " +------\n")
    return

print_header("Control and Evaluations")

def age_group(age):
    """Takes an age(int) in and returns the name of the age group"""
    # Filter the input and print out an age category     
    if age >= 65:
        return "senior"
    elif age >= 18:
        return "adult"
    elif age >= 13:
        return "teen"
    else:
        return "child"
    
def factorial(num):
    """Returns the factorial of passed number"""
    # Get the factorial of the number
    result = num
    for i in range(1, num): # Numbers in range 1 to num-1
        result *= num-i
        
    return result

def get_evens(numbers):
    """Takes in a list of integers and returns all integers in that list that are even."""
    return [x for x in numbers if x%2==0] # Return the list

def count_uniqe(iterable):
    """Takes in an iterable and counts the ammount of each unique item in the list, returns a dictionary."""
    output = {}
    for x in iterable:
        # Count the ammount of time that item appeared in the iterable
        if output.get(x, 0) > 0: # handle if the value does not exist
            output[x] += 1 
        else:
            output[x] = 1
            
    return output

def split_to_tuple(str):
    """Takes in a string and splits it into a tuple."""
    return tuple([x.strip() for x in str.split(',')])

def search_dictionary(dict, search_term, similar = 65):
    """
    takes in a dictionary to search and a search term.
    
    Will return a dictionary of terms that either have the exact
    value searched, are at least given percent similar similar 
    (in letters contained).
    """
    
    output = {}
    for key, value in dict.items():
        # Check if the search term is in the current key
        key_counts = count_uniqe(key.lower())
        search_counts = count_uniqe(search_term.lower())
        
        letters_similar = 0
        for letter in search_counts.keys():
            if letter in key.lower(): letters_similar += search_counts[letter] / key_counts[letter]

                

        if len(search_term) > len(key):
            # Make sure short words don't show up just beause a long word contains it
            if letters_similar/(len(key)+(len(search_term)-len(key))) >= similar/100:
                output[key] = (value, letters_similar/(len(key)+(len(search_term)-len(key))))
        else:
            if letters_similar/len(key) >= similar/100:
                output[key] = (value, letters_similar/len(key))            
    return output
            
    
    
# Loop through until the user enteres a valid integer input
while True:
    # Get user input
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Value entered is not an integer.\n")
   
print(f"\nYou are a {age_group(age)}")

input("\n Press Enter to Continue...")
print_header("Control and Evaluations")
    
# Loop through until the user enteres a valid integer input
while True:
    # Get user input
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Value entered is not an integer.\n")
        
print(f"\nThe factorial of {num} is {factorial(num)}")

input("\n Press Enter to Continue...")
print_header("Control and Evaluations")

# Get the password created by the user
password = input("Create a password: ")
print_header("Control and Evaluations") # Clear screen

# Loop through until the password entered is correct
while True:
    # Check if the password entered is correct
    if input("Enter your password: ") == password:
        break
    else:
        # Print a message when password is incorrect
        print("Incorrect, try again.\n")
        
# Print a confirmation message
print("password entered is correct.")

input("\n Press Enter to Continue...")
print_header("Control and Evaluations")

# Loop through until the password entered is correct
# Uses password created in first part
while True:
    # Check if the password entered is correct
    try:
        if input("Enter your password: ") == password:
            break
        else:
            # Print a message when password is incorrect
            print("Incorrect, try again.\n")
    except KeyboardInterrupt:
        pass
        
# Print a confirmation message
print("password entered is correct.")

input("\n Press Enter to Continue...")
print_header("Data Agregates")

numbers = list(range(0, 11)) # Numbers between 0 and 10
print(f"Numbers: {numbers}")
print(f"Even numbers from number list: {get_evens(numbers)}")

input("\n Press Enter to Continue...")
print_header("Data Agregates")

counts = count_uniqe(split_to_tuple(input("Enter items (seperate with commas): ")))

print('\nItem Counts:')
for k, v in counts.items():
    print(f"  '{k}' - {v}")

input("\n Press Enter to Continue...")
print_header("Data Agregates")

dictionary = {}
# Loop through and allow user to add terms to dictionary
print("Add terms to dictionary, press ctrl + c at any time to quit.")
while True:
    try:
        key = input("Enter a term: ")
        value = input("Etnter definition: ")
        
        dictionary[key] = value
    except KeyboardInterrupt:
        break
    
print_header("Data Agregates") # Clear screen
    
# Loop trhough and allow user to search for terms.
print("Search for terms in dictionary, press ctrl + c at any time to quit.")
while True:
    try:
        # Get search term from user
        search = input("Enter a term to search: ")
        
        print(search_dictionary(dictionary, search))
    except KeyboardInterrupt:
        break
    
input("\n Press Enter to Continue...")
