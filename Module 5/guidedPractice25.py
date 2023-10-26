# Zachary Hoover || 10-17-23 || Guided Practice #25

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

print_header("Indexing, Slicing & Immutability intro")

one_piece = "Monkey D. luffy"

first_character = one_piece[0]
print(first_character) # Output: "M"

print()

fith_character = one_piece[4]
print(fith_character) # Output: "e"

print()

piece = one_piece[4:]
print(piece) # Output: "ey D. Luffy"

print()

new_string = one_piece[0].upper()+one_piece[1:]
print(new_string) # Output: "Monkey D. Luffy"

input("\n Press Enter to Continue...")
print_header("Using slice()")

# String Slicing
string = 'ASTRING'

# Using slice constructer
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print(string[s1])
print(string[s2])
print(string[s3])

input("\n Press Enter to Continue...")
print_header("List/Array Slicing")

string = 'COXMILLCHARGERS'

print(string[:7])
print(string[1:5:2])
print(string[-1:-12:-2])
print(string[::-1])

input("\n Press Enter to Continue...")
print_header("Indexing")

username = "RobloxGamer123"
print(username[0]) # R
print(username[6]) # G

print()

game_name = "Welcome to Bloxburg"
print(game_name.index("o"))

print()

favorite_game = "Adopt Me!"
print(favorite_game[-1]) # !
print(favorite_game[-5]) # t

print()

message = "I love playing Roblox"
message = message[:15] + "Adopt Me!" + message[21:]
print(message) # I love playing Adopt Me!

input("\n Press Enter to Continue...")
print_header("Slicing")

username = "RobloxGamer123"
print(username[6:11]) # Output: "Gamer"

print()

game_name = "Welcome to Bloxburg"
print(game_name[::2])

print()

favorite_game = "Adopt Me!"
print(favorite_game[::-1]) # !eM tpodA

input("\n Press Enter to Continue...")
print_header("Immutability")
try:
    my_string = "Hello"
    my_string[0] = "J"
except TypeError as ve:
    print(ve)
    
my_string = "Hello"
new_string = "J" + my_string[1:]
print(new_string)
    
input("\n Press Enter to Continue...")
print_header("Iterating")

my_string = "Hello, World!"
for character in my_string:
    print(character)
    
print()

first_name = "john"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

print()

my_string = "Hello"
my_string *= 3
print(my_string)

print()

password = "secret"
user_input = input("Enter your password: ")
if user_input == password:
    print("Access granted!")
else:
    print("Access denied.")
    
input("\n Press Enter to Continue...")
print_header("In & Not In")

my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list!")
else:
    print("3 is not in the list.")
    
my_list = "Hello, world!"
if 'z' not in my_list:
    print("z is not in the string!")
else:
    print("z is in the string.")
    
input("\n Press Enter to Continue...")