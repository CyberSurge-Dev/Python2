# Zachary Hoover || 8-24-23 || Guided Practice #4

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Nesting")

# Create alien dictionarys
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}

# Nest aliens in list
aliens =[alien_0, alien_1, alien_2]

# Print aliens
print("  Aliens:")
for alien in aliens:
    print(f"   {alien}")

input("\n Press Enter to Continue...")
print_header("Create Aliens")

aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(f"  {alien}")

# Print total
print(f"\n  Total number of aliens: {len(aliens)}")

input("\n Press Enter to Continue...")
print_header("Create Aliens 2")

# Create empty list for aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# Cycle through and change first three aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(f"  {alien}")

input("\n Press Enter to Continue...")
print_header("A List in a Dictionary")

# Store information about pizza being ordered

pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese']
}

# Summarize order
print(f"  You ordered a {pizza['crust']} crust pizza \n  with the following toppings:")

# Print toppings
for topping in pizza['toppings']:
    print(f"   {topping}")

input("\n Press Enter to Continue...")
print_header("Favorite Languages")

# Create dictionary
favorite_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

# Print
for n, l in favorite_languages.items():
    print(f"\n  {n.title()}'s favorite languages are:")
    for lang in l:
        print(f"    {lang.title()}")

input("\n Press Enter to Continue...")
print_header("Dictionary in Dictionary")

# Create dictionary of users
users = {
    'popcornDave':{
        'first':'dave',
        'last':'smith',
        'location':'charlotte'
    },

    'princessRhea':{
        'first':'rhea',
        'last':'kothur',
        'location':'charlotte'
    }
}

# Print users and info
for username, user_info in users.items():
    print(f"\n  Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"    Full name: {full_name.title()}")
    print(f"    Location: {location.title()}")

input("\n Press Enter to Continue...")

