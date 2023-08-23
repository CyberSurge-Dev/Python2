# Zachary Hoover || 8-22-23 || Independent Practice #1

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Glossary 2")

# Create glossary
glossary = {
    'Dictionary':'A collection of key-value pairs that maps from keys to values. The keys can be any immutable type, and the values can be any type.',
    'Key':'A data item that is mapped to a value in a dictionary. Keys are used to look up values in a dictionary.',
    'Key-Value Pair':'One of the pairs of items in a dictionary. Values are looked up in a dictionary by key.',
    'Mapping Type':'A mapping type is a data type comprised of a collection of keys and associated values. Python’s only built-in mapping type is the dictionary. Dictionaries implement the associative array abstract data type.',
    'Deep Copy':'Deep copying creates a completely independent copy of the dictionary and all its nested objects. Modifying the copied dictionary or its values will not affect the original dictionary.',
    'Set':'A set. unlike lists and tuples, is a orderless list of items.',
    'Variable':'A mutable container that can store several types of data in Python.',
    'Tuple':'A immutable list of items defined with parenthesis in Python.',
    'Integer':'A data type in Python that can only be whole numbers',
    'Immutable':'Cannot be changed/altered'
}

# Print terms with for loop
for k,v in glossary.items():
    print(f"  {k}: {v} \n")

input("\n Press Enter to Continue...")
print_header("Rivers")

# create dict of rivers
rivers = {
    'nile':'egypt',
    'amazon':'brazil',
    'yellow':'china',
    'colorado':'the united states'
}

# Print rivers with formating
for k,v in rivers.items():
    print(f"  The {k.title()} river runs through {v.title()}")

input("\n Press Enter to Continue...")
print_header("Polling")

# Create list of people that should take the poll
people = [
    'frank',
    'jen',
    'sarah',
    'jack',
    'john',
    'phil',
    'abigal',
    'lucas',
    'luran'
]

# Create dictionary of people and favorite language
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'abigal':'Lua'
}

# Get the keys from favorite_language
keys = favorite_language.keys()

# loop through people that should take the poll
for person in people:
    # Check if the person has completed the poll and print a response
    if person in keys:
        print(f"  Thank you {person} for completing the poll.")
    else:
        print(f"  {person}, please complete the poll.")

input("\n Press Enter to Continue...")