# Zachary Hoover || 10-25-23 || Independent Practice #28

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

print_header("Batman Characters")

# Create list of characters from Batman
characters = ['Batman', 'Riddler', 'Penguin', 'Carmine Falcone', 'Alfred Pennyworth']

try:
    # using 'with open() as x' will open and close the file automatically
    with open(f'{path}batman.txt', 'w') as file:
        # Write characters from list on different lines
        file.writelines([x+"\n" for x in characters])
        
    # Print the contents of the file
    with open(f'{path}batman.txt', 'r') as file:
        # Read characters from list on different lines
        print("Contents of batman.txt:")
        for line in file.readlines():
            # Print each line in batman.txt, and remove the folowing whitespace
            print(f"  {line.rstrip()}")
        
    # Way to do this by appending with the list
    characters.append('James Gordon')
    # using 'with open() as x' will open and close the file automatically
    with open(f'{path}batman.txt', 'w') as file:
        # Write characters from list on different lines
        file.writelines([x+"\n" for x in characters])
        
    # Way to do this using only open (append mode)
    with open(f'{path}batman.txt', 'a') as file:
        # Append 'Pete Savage' to the end of the file
        file.write('Pete Savage')
        
    # Print the contents of the file
    with open(f'{path}batman.txt', 'r') as file:
        # Read characters from list on different lines
        print("\nContents of updated batman.txt:")
        for line in file.readlines():
            # Print each line in batman.txt, and remove the folowing whitespace
            print(f"  {line.rstrip()}")
        
except FileNotFoundError as fn:
    print(fn)

input("\n Press Enter to Continue...")
print_header("Sweeny Todd")