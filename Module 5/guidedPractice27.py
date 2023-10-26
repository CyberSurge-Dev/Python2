# Zachary Hoover || 10-24-23 || Guided Practice #27

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

print_header("Sets")

set1 = set()
print(f"Initial blank set: {set1}")

# Creating a set with a string
set1 = set("Barbosa and Simba live with Cassandra")
print(f"\nSet with use of string: {set1}")

# Creating a set with use of tuple
t = (
    "Minecraft",
    "Spider-Man 2",
    "The Last of Us",
    "Minecraft",
    "The Legend of Zelda",
    "Super Mario Bros: Wonder",
    "The Last of Us",
    "Call of Duty",
    "Spider-Man 2"
)

print(f"\nSet with use of tuple: {set(t)}")

input("\n Press Enter to Continue...")
print_header("Creating Sets from Dictionaries")

student_to_courses = {
    'Kyle' : {'Math', 'English'},
    'Sophie' : {'Science', 'Math'},
    'Dustin' : {'History'}
}

input("\n Press Enter to Continue...")
print_header("Fast Membership Testing for Values")

if 'Math' in student_to_courses['Sophie']:
    print("Sophie is enrolled in Math.")

input("\n Press Enter to Continue...")
print_header("Eliminating Duplicates Across Multiple Keys")

all_courses = set()
for courses in student_to_courses.values():
    all_courses.update(courses)
    
print(f"Here are all the courses offered: {all_courses}")

input("\n Press Enter to Continue...")
print_header("Key Membership Test")

another_student_to_courses = {
    'Kyle' : {'Art', 'Music'},
    'Ruthvika' : {'Math', 'Science'},
    'Tyler' : {'History'}
}

common_students = student_to_courses.keys() & another_student_to_courses.keys()
print(f"Common students: {common_students}")

input("\n Press Enter to Continue...")
print_header("Removing and Adding Elements From a Set")

set = set(["Barbosa", "Simba", "Cassandra", "Deepthi", "Cassandra", "Deepthi"])
print(set1)
try:
    set1.remove("Cassandra") # KeyError raised if not found
    print(set1)
except KeyError as k:
    print(k)
# or
set1.discard("Cassandra") # Removes element if found
print(set1)

print()
set1.add("Sinchana")
print(set1)

input("\n Press Enter to Continue...")
print_header("Unions")

# Create 2 sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union of the two sets
union = set1.union(set2)

# Print union
print(union)

print()

# Create 2 sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union of the two sets using '|' opperator
union = set1 | set2

# Print the union set
print(union)

input("\n Press Enter to Continue...")
print_header("Intersections")

# Create 2 sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Intersection of the two sets
intersection = set1.intersection(set2)

# Print the intersection set
print(intersection)

print()

# Create 2 sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

intersection = set1 & set2
# Print the intersection
print(intersection)

input("\n Press Enter to Continue...")
print_header("Difference")

# Create 2 sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Difference of set1 and set2
difference = set1.difference(set2)
# print the difference
print(difference)

print()

# Create 2 sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# difference of set1 and set2 using '-'
difference = set1-set2
print(difference)

input("\n Press Enter to Continue...")
print_header("Set Comprehension")

# Set comprehension to create a set of squares of even numbers from 1 to 10
squares_of_evens = {x**2 for x in range (1, 11) if x % 2 == 0}
print(squares_of_evens)

input("\n Press Enter to Continue...")