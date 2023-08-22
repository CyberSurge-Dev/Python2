# Zachary Hoover || 8-22-23 || Independent Practice #1

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Person")

# Create person dict.
person = {
    'first_name':'Zachary', 
    'last_name':'Hoover', 
    'age':16,
    'city':'Concord'
}

# Print information from person dict.
print("  Person")
print(f"   First Name: {person['first_name']}")
print(f"   Last Name: {person['last_name']}")
print(f"   Age: {person['age']}")
print(f"   City: {person['city']}")

input("\n Press Enter to Continue...")
print_header("Favorite Numbers")

# Create dict. for favorite_nums
favorite_numbers = {
    'John':5,
    'Jack':44,
    'Jill':13,
    'Maddie':7,
    'Jerry':31
}

# Print key-value pairs
for k in favorite_numbers:
    print(f"  {k}'s favorite # is {favorite_numbers[k]}")
    
input("\n Press Enter to Continue...")
print_header("Glossary 1")

# Create dictionary
glossary = {
    'Dictionary':'A collection of key-value pairs that maps from keys to values. The keys can be any immutable type, and the values can be any type.',
    'Key':'A data item that is mapped to a value in a dictionary. Keys are used to look up values in a dictionary.',
    'Key-Value Pair':'One of the pairs of items in a dictionary. Values are looked up in a dictionary by key.',
    'Mapping Type':'A mapping type is a data type comprised of a collection of keys and associated values. Python’s only built-in mapping type is the dictionary. Dictionaries implement the associative array abstract data type.',
    'Deep Copy':'Deep copying creates a completely independent copy of the dictionary and all its nested objects. Modifying the copied dictionary or its values will not affect the original dictionary.'
}

# Print terms with for loop
for k in glossary:
    print(f"  {k}: {glossary[k]} \n")

input("\n Press Enter to Continue...")