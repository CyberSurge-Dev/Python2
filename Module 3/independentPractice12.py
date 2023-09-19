# Zachary Hoover || 9-12-23 || Independent Practice #10

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import math

print_header("Shoryuken!!!!")

def calculate_damage(attack_power, defense_power):
    """Returns the ceiling of attack_power / defense_power."""
    
    return math.ceil(attack_power / defense_power)

# create two int vars
ryu_attack = 50
guile_defense = 20

# Calculate the damage using the vars
damage = calculate_damage(ryu_attack, guile_defense)

# Print out a message using the calculation
print(f"  The damage dealt is {damage}")

input("\n Press Enter to Continue...")
print_header("Gravity")

def calculate_jump_height(gravity, time):
    """Returns the gravity multiplied by time to the power of 2 devided by 2."""
    
    return math.floor(gravity * time**2 / 2)
    

# Create 2 int vars
gravity = 9.8
time = 3

# get jump height
height = calculate_jump_height(gravity, time)

# Print message with jump height
print(f"  The character jumped a height of {height}")

input("\n Press Enter to Continue...")
print_header("Ken is a Clone")

class Character():
    """Simple class to model a character and it's attributes"""
    def __init__(self, name, health, attack_power, defense_power):
        """Initializes the character class."""
        
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense_power = defense_power
        
    def display_stats(self):
        """Prints the attributes of the character"""
        
        # Print details
        print("  Name:", self.name)
        print("  Health:", self.health)
        print("  Attack Power:", self.attack_power)
        print("  Defense Power:", self.defense_power)
        
    def attack(self, character):
        """Takes in another character and uses the attributes from to calculate damage delt, than deducts that from the oher character"""
        # Deduct the other characters health by calculated damage
        character.health -= math.ceil(self.attack_power / character.defense_power)

# Create ryu character object
ryu = Character("Ryu", 100, 30, 30)
# Create ken character object
ken =  Character("Ken", 100, 25, 25)

# Print player stats of both players
ryu.display_stats()
print() # Spacer
ken.display_stats()

# Call attack from ryu
ryu.attack(ken)

print("\n  Ryu attacked Ken! \n")

# Print player stats of both players
ryu.display_stats()
print() # Spacer
ken.display_stats()

input("\n Press Enter to Continue...")
