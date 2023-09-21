# Zachary Hoover || 9-20-23 || Guided Practice #14

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# imports
import random
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("Choice Introduction")

fruits = ['apple', 'bannana', 'orange', 'mango', 'kiwi']
random_fruit = random.choice(fruits)
print("  The randomly selected fruit is:", random_fruit)

input("\n Press Enter to Continue...")
print_header("choice() - Example 1")

wwe_wrestlers = ['John Cena', 'The Rock', 'Stone Cold Steve Austin', 'Triple H', 'Undertaker']
random_wwe_wrestler = random.choice(wwe_wrestlers)
print(f"  The randomly selected WWE wrestler is: {random_wwe_wrestler}")


input("\n Press Enter to Continue...")
print_header("choice() - Example 2")

aew_wrestlers = ['Chris Jericho', 'Jon Moxley', 'Darby Allin', 'Kenny Omega', 'Sting']
random_aew_wrestler = random.choice(aew_wrestlers)
print(f"  The randomly selected AEW wrestler is: {random_aew_wrestler}")

input("\n Press Enter to Continue...")
print_header("choice() - Example 3")

wwe_wrestlers = ['Austin Theory', 'Brock Lesnar', 'Johny Gargano', 'Thomaso Ciampa', 'Roman Reigns']
rand_wwe1 = random.choice(wwe_wrestlers)
rand_wwe2 = random.choice(wwe_wrestlers)

while rand_wwe1 == rand_wwe2:
    rand_wwe2 = random.choice(wwe_wrestlers)
    
print(f'  The randomly selected WWE match between {rand_wwe1} and {rand_wwe2}')

input("\n Press Enter to Continue...")
print_header("choice() - Example 4")

aew_teams = [
    ['Jon Moxley', 'Wheeler Yuta', 'Claudio Castagnoi'],
    ['Nick Jackson', 'Matt Jackson', 'Kenny Omega'],
    ['Pac', 'Penta El Zero Midedo', 'Rey Fenix']
]

rand_team1 = random.choice(aew_teams)
rand_team2 = random.choice(aew_teams)

while rand_team1 == rand_team2:
    rand_team2 = random.choice(aew_teams)
    
print('  The randomly selected AEW trios Tag team math is between ' + rand_team1[0] + ', ' + rand_team1[1] + ', ' + rand_team1[2] + ', and ' + rand_team2[0] + ', ' + rand_team2[1] + ', ' + rand_team2[2])

input("\n Press Enter to Continue...")
print_header("sample() - Example 1")

weapons = ['Poltergust G-OO', 'Strobulb', 'Dark-Light device', 'Suction Shot']
random_weapon = random.sample(weapons, k=1)

print(f'  The randomly selected weapon is: {random_weapon}')

input("\n Press Enter to Continue...")
print_header("sample() - Example 2")

gems = ['Diamond', 'Ruby', 'Emerald', 'Sapphire']
random_gems = random.sample(gems, 2)

print(" ", random_gems)

input("\n Press Enter to Continue...")
print_header("sample() - Example 3")

floors = ["B1", "2F", "5F", "8F", "10F"]
random_floors = random.sample(floors, k=len(floors))

print(" ", random_floors)

input("\n Press Enter to Continue...")
print_header("sample() - Example 4")

ghosts = ['Polterkitty', 'Goob', 'Hammers', 'Slinker', 'Kruller', 'Boos']
random_ghost = random.sample(ghosts, 1)

print(" ", random_ghost)

input("\n Press Enter to Continue...")
print_header("Seed Introduction")

random.seed(42)
print(' ', random.random())

print() # Spacer

random.seed(42)
print(' ', random.randint(1, 10))

print() # Spacer

random.seed(1234)
print(' ', random.random())

random.seed(5678)
print(' ', random.random())

input("\n Press Enter to Continue...")