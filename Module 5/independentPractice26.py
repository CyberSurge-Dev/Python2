# Zachary Hoover || 10-23-23 || Independent Practice #26

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

def print_dictionary(dict, title):
    """Prints dictionary passed in"""
    print(title)
    for key, value in dict.items():
        print(f"  {key}: {value}")

print_header("Lambda Function for Alphabetical Toy Sorting")

# Create and print list of toys
toys = ["Doll", "Car", "Ball", "Kite", "Robot", "Puzzle", "Train", "Boat", "Drum"]
print(f"Toys: {toys}")

# Create lambda function to sort list
lambda_sort = lambda x: x.sort() # Uses built in sort method
# Sort the list
lambda_sort(toys)
# Print sorted list
print(f"Sorted toys: {toys}")

input("\n Press Enter to Continue...")
print_header("Map Function with Barney & Friends' Ages")

# Create dictionary of ages and print the ages
ages = {
    'Barney' : 5,
    'Baby Bop' : 3,
    'BJ' : 7,
    'Riff' : 6
}
print_dictionary(ages, "Ages of Barney and Friends:")

# Create new dictionary of ages using map and lambda functions to increment by one
ages = dict(map(lambda k: (k[0], k[1]+1), ages.items())) # ages.items() returns a list of key, value pairs
# Print new dict.
print_dictionary(ages, "\nAges After:")

input("\n Press Enter to Continue...")
print_header("Filter Function to Find Ripe Apples for Baby Bop")

# Create list of weights and print
weights = [120, 150, 80, 130, 170, 90]
print(f"Weights: {weights}")

# Filter the list to check for apples above 100 grams
filtered_weights = list(filter(lambda x: x > 100, weights))
print(f"Filtered weights (>100): {filtered_weights}")

input("\n Press Enter to Continue...")
print_header("Barney & Friends' Alumni")

# Cretate a list of people and print it
people = ["Selena Gomez", "Demi Lovato", "Madison Pettis", "Debby Ryan"]
print(f"Famous Disney actresses: {people}")

# Make actors names lowercase and then filter names with only more than 12 characters
filtered_people = list(filter(lambda x: len(x) > 12, map(lambda x: x.lower(), people)))
# Print filtered list
print(f"Actresses with names longer than 12 characters: {filtered_people}")

input("\n Press Enter to Continue...")