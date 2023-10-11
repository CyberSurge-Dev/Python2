# Zachary Hoover || 10-10-23 || Guided Practice #21

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

print_header("Example of File I/O")

try:
    f = open("my_file.txt", "w")
    try:
        f.write("Writing some data to the file")
    finally:
        f.close()
except IOError:
    print("Error: my_file.txt does not exist, or it can't be opened for output.")
    
input("\n Press Enter to Continue...")
print_header("Finally Block")

while True:
    try:
        print("\nPlease enter two numbers in the prompts below to try division. type 'q' to quit.")
        num1 = int(input('Enter a number: '))
        num2 = int(input("Enter another number: "))
        result = num1 / num2
        print("Result: ", result)
        if num1 == 'q' or num2 == 'q':
            break
        
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        break
    finally:
        # Will run every time regaurdless of exceptions or not
        print("Finally block executed")
        
input("\n Press Enter to Continue...")
print_header("File Handling")

try: 
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    """
    # Causes an error because file is not defined
    if file:
        file.close()
    """
    print("Finally block executed")
    
input("\n Press Enter to Continue...")
print_header("Raise Exception")

try:
    raise TypeError("Invalid Argument")
except TypeError as e:
    print(e)
    
input("\n Press Enter to Continue...")
print_header("Raise Custom Exception")

class CustomException(Exception):
    pass

try:
    raise CustomException("Something Went Wrong")
except CustomException as e:
    print(e)
    
input("\n Press Enter to Continue...")
print_header("Examples")

try:
    age = int(input("Enter your age: "))
    if age < 0:
        ValueError("Age cannot be negative")
except ValueError as ve:
    print(ve)
    
print() # Spacer

try:
    file = open("myfile.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError as fnfe:
    print(fnfe)
    
input("\n Press Enter to Continue...")
print_header("Using Raise with Loops")

my_list = [1, 2, 3, 4, 5]
for num in my_list:
    if num > 3:
        try:
            raise ValueError("Number greater than 3 found in list!")
        except ValueError as ve:
            print(ve)
            
print() # Spacer

x = 10
while x > 0:
    try:
        if x == 5:
            raise ValueError("Number equals 5, stopping loop!")
    except ValueError as ve:
        print(ve)
        break
    print(x)
    x -= 1
        
input("\n Press Enter to Continue...")
print_header("Functions")

def power_level(name, level):
    if level < 0:
        raise ValueError("Power level cannot be negative")
    print(f"{name}'s power level is {level}")
    
# Testing function
power_level("Goku", 9000)
# Will raise a ValueError
try:
    power_level("Vegeta", -8000)
except ValueError as ve:
    print(ve)

input("\n Press Enter to Continue...")
print_header("Classes")

class Saiyan:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level
    
    def increase_power_level(self, ammount):
        if ammount < 0:
            raise ValueError("Power level increase cannot be negative!")
        self.power_level += ammount
        print(f"{self.name}'s power level increased by {ammount}. New power level: {self.power_level}!")
        
# Crating Saiyan objects
goku = Saiyan("Goku", 9000)
vegeta = Saiyan("Vegeta", 8000)

# Testing the method
goku.increase_power_level(500)
# Will raise Value Error
try:
    vegeta.increase_power_level(-300)
except ValueError as ve:
    print(ve)
    
input("\n Press Enter to Continue...")
print_header("Here we Gooooooo!")

def collect_star(star_number, stars_collected):
    if star_number < 1 or star_number > 120:
        raise ValueError("Invalid star number! Mst be between 1 and 120")
    stars_collected[star_number-1] = True
    print(f"You collected {star_number} stars")
    
# Testing the function
stars = [False] * 120
collect_star(64, stars)
try:
    # This will cause a value error
    collect_star(121, stars)
except ValueError as ve:
    print(ve)

print() # Spacer

def use_powerup(powerup, mario_stats):
    if powerup not in mario_stats:
        raise KeyError(f"Invalid powerup '{powerup}'! Available powerups {list(mario_stats.keys())}")
    mario_stats[powerup] += 1
    print(f"Mario used a {powerup} powerup!")
    
# Testing the function
stats = {'coins':10, 'lives':3, 'mushrooms':1}
use_powerup('mushrooms', stats)
try:
    use_powerup("caps", stats) # This will raise a KeyError
except KeyError as ke:
    print(ke)
    
print() # Spacer

def get_star_location(level, star_number):
    star_locations = {
        "Bob-Omb Battlefield" : ("One the floating island", "Blast Away the Wall"),
        "Cool, Cool Mountain" : ("Slip Slidin' Away", "To the Top of the Fortress"),
        "Jolly Roger Bay" : ("Plunder in the Sunken Ship", "Can the Eel Come Out to Play?")
    }
    try:
        location = star_locations[level][star_number-1]
    except (IndexError, KeyError):
        raise ValueError("Invalid level or star number!")
    else:
        print(f"The location of Star {star_number} in {level} is: {location}")
        
# Testing the function
try:
    get_star_location("Bob-Omb Battlefield", 1)
    get_star_location("Cool, Cool Mountain", 3) # This will raise a value error
except ValueError as ve:
    print(f"An error occured: {ve}")
    
input("\n Press Enter to Continue...")