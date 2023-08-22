# Zachary Hoover || 8-21-23 || Independent Practice #1

from ast import While


def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Exercise 1: Concord Attractions")

# Create dictonary
attractions = {
  'NASCAR Hall of Fame':4, 
  'Great Wolf Lodge':3, 
  'SEA LIFE Charlotte':5, 
  'Frank Liske Park':5, 
  'Concord Mills':1
  }

print("  Attractions:", attractions, "\n")

# Print and sort dictonary
for k in sorted(list(attractions.keys())):
  print(f"  {k} \t {attractions[k]}")

input("\n Press Enter to Continue...")
print_header("Exercise 2: Tourist Spots")

# clear attractions
attractions = {}

# Allow user to enter attractions
while True:
  # Get inputs
  name = input("\n  Enter Attraction Name (Enter 'quit' to quit): ")
  if name.lower() == 'quit':
    break
  fee = input("  Enter Attraction Fee: ")

  # add
  attractions[name] = int(fee)

# Print dict.
print("\n  Attractions Entered:")
for k in list(attractions.keys()):
  print(f"   {k} \t ${attractions[k]}")

input("\n Press Enter to Continue...")
print_header("Exercise 3: Restaurant Ratings")

# Create dict for restaurants
restaurants = {
  'Johnny Rogers':4.0,
  'Birritaco':4.5,
  "Lil Papi's International Deli":5.0,
  'The Smoke Pit':4.5,
  'Havana Carolina':4.0,
  'Benny DaCorsas':4.0,
  'La Autentica':4.7
}

# Print items for user
print("  Restaurants:")
for k in list(restaurants.keys()):
  print(f"   {k}")

# Allow user to search until quit
while True:
  inp = input("\n  Enter a restaurant to search (enter 'quit' to quit): ")

  # Check and get rating
  if inp.lower() == 'quit':
    break
  else:
    # Print rating if found.
    print(f"  Rating: {restaurants.get(inp, 'No rating found.')}")







