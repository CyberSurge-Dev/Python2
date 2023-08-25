# Zachary Hoover || Mini Project: Dictionary
# 8-25-23 

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Task 1 - Alphabetical Order")

# Get users input 
usr_in = input("  Enter a sentance: ")

# Create dictionary for letter counts
counts = {}

# Loop through sentance for characters
for letter in list(usr_in):
    if letter.isalpha():
        if counts.get(letter, False) != False:
            counts[letter.lower()] += 1
        else:
            counts[letter.lower()] = 1

# Cycle through sorted keys and print in alphabetical order
print("\n  Letter count:")
for key in sorted(list(counts.keys())):
    print(f"    {key} - {counts[key]}")

input("\n Press Enter to Continue...")
print_header("Task 1 - Alphabetical Order")


def translator(sentance):
    """This function translates any string passed in, in to pirate speak and returns the result."""
    
    # Dictionary for translation
    pirate_translator = {
        'sir':'matey',
        'hotel':'fleabag inn',
        'student':'swabbie',
        'boy':'matery',
        'madam':'proud beauty',
        'professor':'foul blaggart',
        'restaurant':'galley',
        'your':'yer',
        'excuse':'arr',
        'students':'swabbies',
        'are':'be',
        'lawyer':'foul blaggart',
        'the':'th',
        'restroom':'head',
        'my':'me',
        'hello':'avast',
        'is':'be',
        'man':'matey'
    }
    # Make all characters lowercase
    sentance = sentance.lower()
    # Index placeholder variable
    index = 0
    # Split words from sentance into a list using split()
    sentance = sentance.split(' ')
    # Cycle through words in the list using for loop
    for word in sentance:
        # check if there is a translation
        if word in list(pirate_translator.keys()):
            # Replace the word in the list
            sentance[index] = pirate_translator[word]
        index += 1
        
    # Repack sentance into a string
    out_str = ""
    for word in sentance:
        out_str += (word+" ")
        
    # Return new sentance
    return out_str

# Get user input
usr_in = input("  Enter a sentance (no punctuation): ")
# Print out the result from the translator function
print(f"\n  Translated:\n  {translator(usr_in)}")

input("\n Press Enter to Continue...")
