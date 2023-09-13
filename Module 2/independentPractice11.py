# Zachary Hoover || 9-12-23 || Independent Practice #10

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Task 1")

class SmashFighter:
    """Simple class to model Smash Fighter."""
    def __init__(self, name, main_weapon):
        """Initialize SmashFighter with name and manin_weapon (private)."""
        self.name = name
        self.__main_weapon = main_weapon

# Create instance
smashFighter = SmashFighter("Link", "Master Sword")
# Print message using instance and access private variable
print(f"  {smashFighter.name}'s main weapon is {smashFighter._SmashFighter__main_weapon}")

input("\n Press Enter to Continue...")
print_header("Task 2")

class Pokemon:
    """Simple class to model a Pokemon."""
    def __init__(self, name, type):
        """Initialize Pokemon class"""
        self.name = name
        self._type = type

# Create instance
pokemon = Pokemon("Pikachu", "Electric")
print(f"  {pokemon.name} is a(n) {pokemon._type} Pokemon.")

input("\n Press Enter to Continue...")
print_header("Task 3")

class MarioCharacter:
    """Simple class to model a mario character."""
    def __init__(self, name, powerup):
        """Initialize the MarioCharacter class with name and powerup."""
        self.__name = name
        self.__powerup = powerup
        
# Create instance of MarioCharacter
mario = MarioCharacter("Mario", "Fire Flower")

print(f"  {mario._MarioCharacter__name} has the powerup: {mario._MarioCharacter__powerup}")

input("\n Press Enter to Continue...")
print_header("Task 4")

class FinalFantasyCharacter:
    """Simple class to model a Final Fantasy character."""
    def __init__(self, name, level):
        """Initializes class with name and level arguments."""
        self.name = name
        self.__level = level
        
    def get_level(self):
        """Returns the level that the character is at."""
        return self.__level
    
# Create instance of the class
cloud = FinalFantasyCharacter("Cloud", 50)
print(f"  {cloud.name} is at level {cloud.get_level()}")

input("\n Press Enter to Continue...")
print_header("Task 5")

class ZeldaCharacter:
    """Simple class to model a Zelda Character."""
    def __init__(self, name, health):
        """Initialize ZeldaCharacter"""
        self.name = name
        self.__health = health
        
    def get_health(self):
        """Returns the health of the character."""
        return self.__health
    
    def set_health(self, health):
        """Sets the chaeacters health to the provided int."""
        self.__health = health

# Create instance and set health to 100
link = ZeldaCharacter("Link", 100)
print("  Current health:", link.get_health(), "hp")
print(f"  {link.name} was hit for 25hp!")

# Set health to 75
link.set_health(75)

# Print new health
print("  Current health:", link.get_health(), "hp")
        
input("\n Press Enter to Continue...")
print_header("Task 6")

class PokemonTrainer:
    """Simple class to model a pokemon trainer."""
    def __init__(self, name, *pokemon):
        """Initialize the class with name and pokemon list."""
        self.name = name
        self.__pokemon_list = pokemon
        
    def get_pokemon_list(self):
        """Returns the trainers list of pokemon"""
        # Convert tuple to list and return value
        return list(self.__pokemon_list)

# Create instance of the class with pokemon
trainer = PokemonTrainer("Ash", "Pikachu", "Charmander")
# Print a message using the class
print(f"  {trainer.name}'s pokemon list: {trainer.get_pokemon_list()}")
    
input("\n Press Enter to Continue...")