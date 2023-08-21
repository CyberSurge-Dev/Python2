# Zachary Hoover || 8-21-23 || Guided Practice #1

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Dictonary Intro")

eng2sp = {}

# Create a dictonary with items
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

print(" ", eng2sp)
input("\n Press Enter to Continue...")
print_header("Another Way")

# One line create dict.
eng2sp = {'three':'tres', 'one':'uno', 'two':'dos'}
print(" ", eng2sp)

input("\n Press Enter to Continue...")
print_header("Looking up values")

# Print a value from dict.
value = eng2sp['two']
print(' ', value)

input("\n Press Enter to Continue...")
print_header("DEL")

# Create dict. deleter an item
inventory = {'apples':430, 'bananas':312, 'oranges':525, 'pears':217}
print(' ', inventory)

del inventory['pears']

print('\n ', inventory)

input("\n Press Enter to Continue...")
print_header("MUTABLE")

# Print the dict.
inventory = {'apples':430, 'bananas':312, 'oranges':525, 'pears':217}
print(' ', inventory)

# Change a value in dict.
inventory['pears'] = 0

print('\n ', inventory)

input("\n Press Enter to Continue...")
print_header("ADDING")

inventory = {'apples':430, 'bananas':312, 'oranges':525, 'pears':217}
print(' ', inventory)

# Add value to dict. 'bananas'
inventory['bananas'] += 200
print('\n ', inventory)

# Print size of dictonary
numitems = len(inventory)
print("  Lenth of dictonary:", numitems)

input("\n Press Enter to Continue...")
print_header("Meathods")

inventory ={'apples':430, 'bananas':312, 'oranges':525, 'pears':217}

# Print out all values using for loop.
for akey in inventory.keys(): # Get keys of dictonary
    print("  Got key", akey, "which maps to", inventory[akey])

# print keys
ks = list(inventory.keys())
print("  Keys:", ks)

input("\n Press Enter to Continue...")
print_header("Keys")

inventory ={'apples':430, 'bananas':312, 'oranges':525, 'pears':217}

# Print keys
for k in inventory:
    print("  Got key", k)

input("\n Press Enter to Continue...")
print_header("Values/Items")

inventory ={'apples':430, 'bananas':312, 'oranges':525, 'pears':217}

# Print values and items
print(" ", list(inventory.values()))
print(" ", list(inventory.items()))

for (k,v) in inventory.items():
    print("  Got",k,"that maps to",v)

for k in inventory:
    print("  Got",k,"that maps to", inventory[k])

input("\n Press Enter to Continue...")
print_header("In/Not In")

# Booleans if
inventory = {'apples':430, 'bananas':312, 'oranges':312, 'pears':217}
print(" ", 'apples' in inventory)
print(" ", 'cherries' in inventory)

if 'bananas' in inventory:
    print(" ", inventory['bananas'])
else:
    print('  We have no bananas')

input("\n Press Enter to Continue...")
print_header("get")

inventory = {'apples':430, 'bananas':312, 'oranges':312, 'pears':217}

# Using Get
print(" ", inventory.get("apples"))
print(" ", inventory.get("cherries"))
print(" ", inventory.get("cherries", 0))

input("\n Press Enter to Continue...")
print_header('Aliasing')

# Create alias
opposites = {'up':'down', 'right':'wrong', 'true':'false'}
alias = opposites

# Print boolean
print("  Is alias opposites?", alias is opposites)

# Change alias
alias['right'] = 'left'
print(" ", opposites['right'])

input("\n Press Enter to Continue...")
print_header("Copying")

acopy = opposites.copy()

# Alter the copy
acopy['right'] = 'left'
print(" ", acopy['right'])

input("\n Press Enter to Continue...")
