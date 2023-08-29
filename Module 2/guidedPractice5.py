# Zachary Hoover || 8-29-23 || Guided Practice #5

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("OOP in Simple Terms")

# This is like a cookie cutter
class Superhero:
    health = 100
    speed = 10
    
ironman = Superhero()
print(" ", ironman.health)

# Extending a class
class SuperheroWithSpecialMove(Superhero):
    special_move = "Laser Beam"
    
# Details about super hero with spwcial move
print("\n  SuperheroWithSpecialMove:")
print("   Health:", SuperheroWithSpecialMove.health)
print("   Speed:", SuperheroWithSpecialMove.speed)
print("   Special move:", SuperheroWithSpecialMove.special_move)
    
input("\n Press Enter to Continue...")
print_header("Class Special Properties")

# Dog class
class Dog:
    pass

print("  Name of class:", Dog.__name__)
# If this class was in a file called animals.py
print("  Module of Dog:", Dog.__module__) # This would print animals

# Class Puppy inherits attributes fromm class Dog
class Puppy(Dog):
    pass

# Print it out
print("  Puppy bases:", Puppy.__bases__) # Prints bases

input("\n Press Enter to Continue...")
print_header("Creating the Dog Class")

class Dog:
    """A simple attempt to model Dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a Dog sitting in response to command."""
        print(f"  {self.name} is now sitting")
        
    def roll_over(self):
        """Simulate rolling over in response to command."""
        print(f"  {self.name} rolled over!")

my_dog = Dog('Fipps', 7)

print(f"  My dog's name is {my_dog.name}.")
print(f"  My dog is {my_dog.age} years old.\n")

# Calling methods from class
my_dog.sit()
my_dog.roll_over()

input("\n Press Enter to Continue...")
print_header("Multiple Instances")

my_dog = Dog("Fipps", 7)
your_dog = Dog("Lucy", 3)

print(f"  My dog's name is {my_dog.name}.")
print(f"  My dog is {my_dog.age} years old.")
my_dog.sit()

print("")
print(f"  Your dog's name is {your_dog.name}.")
print(f"  Your dog is {your_dog.age} years old.")
your_dog.sit()

input("\n Press Enter to Continue...")