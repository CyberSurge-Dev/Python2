# Zachary Hoover || 8-21-23 || Guided Practice #2

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Alien Dictionary")

# Create dict.
alien_0 = {'color':'green', 'points':5}

# Print values
print("  Alien color:", alien_0['color'])
print("  Alien points:", alien_0['points'])

input("\n Press Enter to Continue...")
print_header("Alien Accessing Values")

# Assign value to variabe and print
new_points = alien_0['points']
print(f"  You just earned {new_points} points!")

input("\n Press Enter to Continue...")
print_header("Alien Adding New Key-Value Pairs")

# Create dict.
alien_0 = {'color':'green', 'points':5}
print("  Alien_0:", alien_0)

# add new pairs
alien_0['x_poistion'] = 0
alien_0['y_poistion'] = 25

print("  Alien_0:", alien_0)

input("\n Press Enter to Continue...")
print_header("Alien Starting w/ Empty Dictionary")

# Create empty dict.
alien_0 = {}

# add items to dict.
alien_0['color'] = 'green'
alien_0['points'] = 5

print("  Alien_0:", alien_0)

input("\n Press Enter to Continue...")
print_header("Alien Modifying Values")

# Create dict.
alien_0 = {'color':'green'}

# Print color
print(f"  The alien is {alien_0['color']}.")

# Change color and print
alien_0['color'] = 'yellow'
print(f"  The alien is {alien_0['color']}.")

input("\n Press Enter to Continue...")
print_header("Alien Modifying Values 2")

alien_0 = {
    "x_position":0, 
    "y_position":25,
    "speed":"medium"
}

print(f"  Original position: {alien_0['x_position']}")

x_increment = 0
# Move the alien to the right
# Determine how far to move the alien based on current speed.

if alien_0['speed'] == 'slow':
    x_increment += 1
elif alien_0['speed'] == 'medium':
    x_increment += 2
else:
    x_increment += 3

alien_0['x_position'] += x_increment

print(f"  The alien has moved to: {alien_0['x_position']}")

input("\n Press Enter to Continue...")
print_header("Alien Removing Pairs")

# Create and print alien_0
alien_0 = {'color':'green', 'points':5}
print("  Alien_0:", alien_0)

# Delete item
del alien_0['points']

# Print again
print("  Alien_0 again:", alien_0)

input("\n Press Enter to Continue...")
print_header("Alien Using get()")

alien_0 = {'color':'green', 'speed':'slow'}
# Will cause an Error: KeyError
# print(" ", alien_0['points'])

# Proper way
print(" ", alien_0.get('points', 'No point value assigned in alien_0.'))

input("\n Press Enter to Continue...")