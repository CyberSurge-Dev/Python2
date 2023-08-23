# Zachary Hoover || 8-21-23 || Guided Practice #2

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Filling Dict. With Input")

# Set loop active
polling_active = True
responses = {}

while polling_active:
    # Prompt user for first name and response
    name = input("  What is your name?: ")
    res = input("  Which mountain would you like to climb someday?: ")

    # Store the response in a dictonary
    responses[name] = res

    rep = input("  Would you like to submit another response (y/n)?: ")
    if rep.lower() == 'no' or rep.lower() == 'n':
        # Redundent variable set to false
        polling_active = False
        # Break the loop (the variable is useless)
        break

# Polling is complete, show results
print_header("Poll Results")
for k, v in responses.items():
    print(f"  {k} would like to climb {v}.")

input("\n Press Enter to Continue...")
print_header("Loops")

# Create dict.
user_0 = {
    'username':'chefsushi',
    'first':'sushantha',
    'last':'yarlagadda'
}

# Print values
for key, value in user_0.items():
    print(f"\n  Key: {key}")
    print(f"  Value: {value}")

input("\n Press Enter to Continue...")
print_header("Fav Languages")

# Create dict.
favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

# Print dict.
for name, lang in favorite_language.items():
    print(f"  {name.title()}'s favorite language is {lang.title()}")

input("\n Press Enter to Continue...")
print_header("All the keys")

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}

# Print keys only
print("  Keys only:")
for name in favorite_language.keys():
    print(f"   {name.title()}")

# Create list of friends
friends = ['phil', 'sarah']

print("\n  Keys and languages:")
for name in favorite_language.keys():
    print(f"   Hello, {name}")

    # Check for friends
    if name in friends:
        language = favorite_language[name].title()
        print(f"   {name.title()}, I see you love {language}")

if 'erin' not in favorite_language.keys():
    print("\n  Erin, please take our poll")

input("\n Press Enter to Continue...")
print_header("Particular Order (sorted)")

# Print keys sorted
for name in sorted(favorite_language.keys()):
    print(f"  {name.title()}, thank you for taking the poll.")

input("\n Press Enter to Continue...")
print_header("All Values")

# Print values
print("  The following lanuages have been mentioned:")
for language in favorite_language.values():
    print("  ", language.title())

# Print values using sets
print("\n  The following lanuages have been mentioned:")
for language in set(favorite_language.values()):
    print("  ", language.title())

input("\n Press Enter to Continue...")




