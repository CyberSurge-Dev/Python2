# Zachary Hoover || 8-24-23 || Independent Practice #4

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("People")

# Create dict. for person 1
person_1 = {
    'first_name':'Zachary', 
    'last_name':'Hoover', 
    'age':16,
    'city':'Concord'
}

# Create dict. for person 2
person_2 = {
    'first_name':'James', 
    'last_name':'jackson', 
    'age':22,
    'city':'New Hampshire'
}

# Create dict. for person 3
person_3 = {
    'first_name':'Katlyne', 
    'last_name':'Hoover', 
    'age':20,
    'city':'Washington DC'
}

# Create list to store the people
people = [person_1, person_2, person_3]

# Print people and their details
for person in people:
    print(f"\n  First Name: {person['first_name'].title()}")
    print(f"  Last Name: {person['last_name'].title()}")
    print(f"  Age: {person['age']}")
    print(f"  City: {person['city'].title()}")

input("\n Press Enter to Continue...")
print_header("Pets")

# Create dictionarys pets
pet_0 = {
    'owners_name':'Jack',
    'animal':'dog',
    'name':'fipps',
    'age':7
}

pet_1 = {
    'owners_name':'Jack',
    'animal':'cat',
    'name':'tigger',
    'age':19
}

pet_2 = {
    'owners_name':'Jack',
    'animal':'turtle',
    'name':'sheldon',
    'age':3
}

# Store pets in a list
pets = [pet_0, pet_1, pet_2]

# Loop through and print all pets
for pet in pets:
    print(f"\n  Owner name: {pet['owners_name'].title()}")
    print(f"  Animal type: {pet['animal'].title()}")
    print(f"  Pet name: {pet['name'].title()}")
    print(f"  Pet age: {pet['age']}")

input("\n Press Enter to Continue...")
print_header("Favorite Places")

favorite_places = {
    'james':['grand canyon', 'bahamas', 'mexico'],
    'jack':['england', 'germany', 'canada'],
    'jerry':['florida', 'france', 'australia']
}

# Print people and their favorite places
for k in favorite_places.keys():
    print(f"\n  {k}'s favorite places are:")

    places = favorite_places[k]
    for place in places:
        print(f"    {place}")

input("\n Press Enter to Continue...")
print_header("Favorite Numbers")

# Create dictionary for favorite numbers
favorite_numbers = {
    'John':[5, 7, 13],
    'Jack':[44, 32, 7],
    'Jill':[13, 33, 333],
    'Maddie':[21, 7, 9],
    'Jerry':[21, 42, 36]
}

# Print people and their favorite numbers
for k in favorite_numbers.keys():
    print(f"\n  {k}'s favorite numbers are:")
    numbers = favorite_numbers[k]
    for number in numbers:
        print(f"    {number}")

input("\n Press Enter to Continue...")
print_header("Cites")

# Create nested dictionaries for cities
cities = {
    'charlotte':{
        'country':'the united states',
        'population':'879 thousand',
        'fact':'nicknamed "queen city"'
    },
    'atlanta':{
        'country':'the united states',
        'population':'469 thousand',
        'fact':'home to the worlds busiest airport'
    },
    'sydney':{
        'country':'australia',
        'population':'5.312 million',
        'fact':'sydney has over 100 beaches'
    }
}

# Print city and information about city
for city in cities.keys():
    print(f"\n  City: {city}")
    
    # Store info variable
    info = cities[city]

    # Print details
    print(f"    Country: {info['country'].title()}")
    print(f"    Population: {info['population']}")
    print(f"    Fun fact: {info['fact']}")

input("\n Press Enter to Continue...")