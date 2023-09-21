# Zachary Hoover || 9-21-23 || Independent Practice #15

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import random
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print(r"""
               ---- Task 1 ----
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠷⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⣶⣦⣼⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣾⣿⣿⣿⣿⣿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣿⡟⣹⡟⣴⢻⣷⠘⠿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⡿⠐⢋⣴⣋⣯⣽⣷⣦⣤⠤⣾⣿⣿⣿⣿⣿⣿⠻⢿⣿⣿⣿⣿⣿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⣒⡻⠟⣿⣨⣿⠉⠉⠐⣲⣿⣿⣿⣿⣿⣿⣿⠀⠀⠉⠙⠛⠻⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣷⡤⣢⢹⠉⣣⣠⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣦⣤⣤⣬⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣿⣿⢿⣡⡆⡤⣭⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠛⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣽⣿⣷⣅⣿⣷⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠛⠈⠙⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⠏⠙⠿⣿⣿⣿⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⢹⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡿⠃⠀⠀⠀⠈⠙⠋⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣷⠀⠀⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣄⠘⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣧⠸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠙⠻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      """)

print_header("Example 1")

# Create a list of enemies
enemies = ["Bokoblin", "Moblin", "Lizalfos", "Lynel", "Hinox", "Wizzrobe", "Guardian", "Yiga Footsoldier", "Talus", "Stalnox", "Hinox (Stalnox)", "Molduga", "Stalker Guardian", "Hyrulean Soldier (Enemy)", "Yiga Blademaster", "Stone Talus", "Igneo Talus", "Frost Talus", "Thunderblight Ganon", "Windblight Ganon", "Waterblight Ganon", "Fireblight Ganon", "Calamity Ganon", "Master Kohga", "Dark Beast Ganon"]
# get 5 random and unique items from the list of enemies
random_enemies = random.sample(enemies, 5)
# Print the list
print(f"  Sample list: {random_enemies}")
# Print out a randomly selected enemy from the list
print(f"  The randomly selected enemy is: {random.choice(random_enemies)}")


input("\n Press Enter to Continue...")
print_header("Example 2")

# Create a list of weapons
weapons = ['Traveler\'s Sword', 'Soldier\'s Broadsword', 'Knight\'s Claymore', 'Boko Club', 'Spiked Boko Club', 'Dragonbone Boko Club', 'Lizal Boomerang', 'Lizal Forked Boomerang', 'Lizal Tri-Boomerang', 'Guardian Sword', 'Guardian Sword+', 'Guardian Sword++', 'Ancient Short Sword', 'Ancient Sword', 'Rusty Broadsword', 'Royal Broadsword', 'Forest Dweller\'s Sword', 'Zora Sword', 'Feathered Edge', 'Gerudo Scimitar', 'Moonlight Scimitar', 'Scimitar of the Seven', 'Eightfold Blade', 'Edge of Duality', 'Serpentine Spear']
# get 5 random and unique items from the list of weapons
random_weapons = random.sample(weapons, 5)
# Print the list
print(f"  Sample list: {random_weapons}")
# Print out a randomly selected weapon from the list
print(f"  The randomly selected weapon is: {random.choice(random_weapons)}")

input("\n Press Enter to Continue...")
print_header("Example 3")

# Create a list of characters
characters = ["Link","Zelda","Mipha","Daruk","Revali","Urbosa","Impa","Purah","Robbie","Sidon","Yunobo", "Teba","Riju","Kass", "Hestu","Master Kohga","Monk Maz Koshia","King Rhoam","Princess Zelda", "Great Deku Tree","King Dorephan","Sergeant Link","Paya", "Beedle","Bolson","Hudson", "Greyson"]
# get 5 random and unique items from the list of characters
random_characters = random.sample(characters, 5)
# Print the list
print(f"  Sample list: {random_characters}")
# Print out a randomly selected character from the list
print(f"  The randomly selected character is: {random.choice(random_characters)}")

input("\n Press Enter to Continue...")
print_header("Example 4")

# Create a list of characters
locations = ["Great Plateau","Hyrule Field","Faron Woods","Eldin Mountains","Gerudo Desert", "Hebra Mountains", "Tabantha Frontier","Akkala Highlands","Lanayru Wetlands", "Mount Lanayru","Zora's Domain","Kakariko Village", "Hateno Village","Rito Village",    "Gerudo Town", "Tarrey Town","Lurelin Village","Satori Mountain", "Shrine of Resurrection","Hylian River","Lake Hylia","Death Mountain", "Lost Woods","Korok Forest", "Akala Island","Eventide Island","Ganondorf's Castle", "The Master Sword"]
# get 5 random and unique items from the list of locations
random_locations = random.sample(locations, 5)
# Print the list
print(f"  Sample list: {random_locations}")
# Print out a randomly selected location from the list
print(f"  The randomly selected location is: {random.choice(random_locations)}")

input("\n Press Enter to Continue...")
print(r"""
               ---- Task 2 ----
   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠷⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⣶⣦⣼⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣾⣿⣿⣿⣿⣿⣟⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣿⡟⣹⡟⣴⢻⣷⠘⠿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⡿⠐⢋⣴⣋⣯⣽⣷⣦⣤⠤⣾⣿⣿⣿⣿⣿⣿⠻⢿⣿⣿⣿⣿⣿⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⣿⣒⡻⠟⣿⣨⣿⠉⠉⠐⣲⣿⣿⣿⣿⣿⣿⣿⠀⠀⠉⠙⠛⠻⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣿⣷⡤⣢⢹⠉⣣⣠⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣦⣤⣤⣬⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣿⣿⢿⣡⡆⡤⣭⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠉⠛⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣽⣿⣷⣅⣿⣷⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠛⠈⠙⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⠏⠙⠿⣿⣿⣿⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⢹⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡿⠃⠀⠀⠀⠈⠙⠋⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣷⠀⠀⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠶⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣄⠘⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣧⠸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠙⠻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      """)

# Set the seed for random 
random.seed(1234567891)

print_header("Example 1")

# Create a list of enemies
enemies = ["Bokoblin", "Moblin", "Lizalfos", "Lynel", "Hinox", "Wizzrobe", "Guardian", "Yiga Footsoldier", "Talus", "Stalnox", "Hinox (Stalnox)", "Molduga", "Stalker Guardian", "Hyrulean Soldier (Enemy)", "Yiga Blademaster", "Stone Talus", "Igneo Talus", "Frost Talus", "Thunderblight Ganon", "Windblight Ganon", "Waterblight Ganon", "Fireblight Ganon", "Calamity Ganon", "Master Kohga", "Dark Beast Ganon"]
# get 5 random and unique items from the list of enemies
random_enemies = random.sample(enemies, 5)
# Print the list
print(f"  Sample list: {random_enemies}")
# Print out a randomly selected enemy from the list
print(f"  The randomly selected enemy is: {random.choice(random_enemies)}")


input("\n Press Enter to Continue...")
print_header("Example 2")

# Create a list of weapons
weapons = ['Traveler\'s Sword', 'Soldier\'s Broadsword', 'Knight\'s Claymore', 'Boko Club', 'Spiked Boko Club', 'Dragonbone Boko Club', 'Lizal Boomerang', 'Lizal Forked Boomerang', 'Lizal Tri-Boomerang', 'Guardian Sword', 'Guardian Sword+', 'Guardian Sword++', 'Ancient Short Sword', 'Ancient Sword', 'Rusty Broadsword', 'Royal Broadsword', 'Forest Dweller\'s Sword', 'Zora Sword', 'Feathered Edge', 'Gerudo Scimitar', 'Moonlight Scimitar', 'Scimitar of the Seven', 'Eightfold Blade', 'Edge of Duality', 'Serpentine Spear']
# get 5 random and unique items from the list of weapons
random_weapons = random.sample(weapons, 5)
# Print the list
print(f"  Sample list: {random_weapons}")
# Print out a randomly selected weapon from the list
print(f"  The randomly selected weapon is: {random.choice(random_weapons)}")

input("\n Press Enter to Continue...")
print_header("Example 3")

# Create a list of characters
characters = ["Link","Zelda","Mipha","Daruk","Revali","Urbosa","Impa","Purah","Robbie","Sidon","Yunobo", "Teba","Riju","Kass", "Hestu","Master Kohga","Monk Maz Koshia","King Rhoam","Princess Zelda", "Great Deku Tree","King Dorephan","Sergeant Link","Paya", "Beedle","Bolson","Hudson", "Greyson"]
# get 5 random and unique items from the list of characters
random_characters = random.sample(characters, 5)
# Print the list
print(f"  Sample list: {random_characters}")
# Print out a randomly selected character from the list
print(f"  The randomly selected character is: {random.choice(random_characters)}")

input("\n Press Enter to Continue...")
print_header("Example 4")

# Create a list of characters
locations = ["Great Plateau","Hyrule Field","Faron Woods","Eldin Mountains","Gerudo Desert", "Hebra Mountains", "Tabantha Frontier","Akkala Highlands","Lanayru Wetlands", "Mount Lanayru","Zora's Domain","Kakariko Village", "Hateno Village","Rito Village",    "Gerudo Town", "Tarrey Town","Lurelin Village","Satori Mountain", "Shrine of Resurrection","Hylian River","Lake Hylia","Death Mountain", "Lost Woods","Korok Forest", "Akala Island","Eventide Island","Ganondorf's Castle", "The Master Sword"]
# get 5 random and unique items from the list of locations
random_locations = random.sample(locations, 5)
# Print the list
print(f"  Sample list: {random_locations}")
# Print out a randomly selected location from the list
print(f"  The randomly selected location is: {random.choice(random_locations)}")

input("\n Press Enter to Continue...")
