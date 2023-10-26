# Zachary Hoover || 10-24-23 || Independent Practice #27

# Imports
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

print_header("Andrew Lloyd Webber")

# Create sets for andrew lloyd webber musicals and plays from the 80s
andrew_lloyd_webber_musicals = {"Joseph and the Amazing Technicolor Dreamcoat", "Jesus Christ Superstar",    "Evita",    "Cats",    "Starlight Express",    "The Phantom of the Opera", "Aspects of Love",    "Sunset Boulevard",    "Whistle Down the Wind",    "The Beautiful Game", "The Woman in White",    "Love Never Dies",    "Stephen Ward",    "School of Rock", "Cinderella"}
# Convert list to a set
plays_80s = set(["Phantom of the Opera", "Barnum", "42nd Street", "Nine", "Little Shop of Horrors","Jerome Robbins' Broadway", "Sunday in the Park with George", "Falsettos", "Heathers: The Musical", "Falsettos", "Merrily We Roll Along", "The Normal", "La Cage aux Folles", "Starlight Express", "Dreamgirls", "The Mystery of Edwin Drood", "Miss Saigon", "Aspects of Love", "Cats", "Sophisticated Ladies", "Angels in America", "Chess", "Torch Song Trilogy", "Signin' in the Rain", "Hurlyburly", "Blood Brothers", "Into the Woods", "Rent", "Madame Butterfly"])

# Create a set that is the interesection of the two sets
# Gets items that are in both sets and stores them in a new set
intersection = andrew_lloyd_webber_musicals & plays_80s

# Print the intersection of the two tuples
print("Plays from the 80s made by Andrew Lloyd Webber:")
for play in intersection:
    print(f"  {play}")

input("\n Press Enter to Continue...")
print_header("Sweeny Todd")

# Cretate sets for Sweent Todd Broadway musical songs, and songs in the movie adaptation
sweeney_todd_broadway = {"The Ballad of Sweeney Todd", "No Place Like London", "The Worst Pies in London", "Poor Thing", "My Friends", "Green Finch and Linnet Bird", "Ah, Miss", "Johanna", "Pirelli's Miracle Elixir", "The Contest", "Wait", "Epiphany", "A Little Priest", "Johanna (Reprise)", "God, That's Good!", "By the Sea", "Not While I'm Around", "Final Sequence"}
# Convert tuple to a set
sweeney_todd_movie = set(("Opening Title", "No Place Like London", "The Worst Pies in London", "Poor Thing", "My Friends", "Green Finch and Linnet Bird", "Alms! Alms!", "Johanna", "Pirelli's Miracle Elixir", "The Contest", "Wait", "Ladies in Their Sensitivities", "Pretty Women", "Epiphany", "A Little Priest", "Johanna (Reprise)", "God, That's Good!", "By the Sea", "Not While I'm Around", "Final Scene"))

# Get the differnce of the two sets (Items that are in sweeney_todd_broadway but not in sweeney_todd_movie)
difference = sweeney_todd_broadway - sweeney_todd_movie

# Print the intersection of the two tuples
print("Songs that were in the musical and not the movie:")
for song in difference:
    print(f"  {song}")
    
# Get the differnce of the two sets (Items that are in sweeney_todd_moviebut not in sweeney_todd_broadway)
difference = sweeney_todd_movie - sweeney_todd_broadway
    
# Print the intersection of the two tuples
print("\nSongs that were in the movie and not the musical:")
for song in difference:
    print(f"  {song}")

input("\n Press Enter to Continue...")