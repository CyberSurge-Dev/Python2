# Zachary Hoover || 9-12-23 || Independent Practice #10

from inspect import getmodule


def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Task 1")

def addition(*nums):
    """Adds up all numbers passed in and returns the result."""
    out = 0
    for num in nums: # loop through and add
        out += num
    
    # Return result
    return out

def multiplication(*nums):
    """Multiplies up all numbers passed in and returns the result."""
    out = 0
    for num in nums: # loop through and multiply
        out *= num
    
    # Return result
    return out

def concatenation(*strings):
    """Concatenates all strings passed in and returns result."""
    out = ""
    for s in strings: # loop through and add strings
        out += s
    
    # Return result
    return out

def print_kwargs(**kwargs):
    """Prints all passed in Kwargs."""

    for k, v in kwargs.items(): # Loop through and print kwargs
        print(f"  {k} : {v}")
        
numbers = (4, 5, 6, 7, 8, 6) # Create tuple of numbers  

print(f"  Numbers for functions: {numbers}") # Print the numbers
print("   Product:", multiplication(*numbers)) # Multiply
print("   Sum:", addition(*numbers)) # add

# Create a tuple of strings
strings = (
    "one",
    "two",
    "three",
    "four",
    "five"
)

print() # Spacer

print("  Strings for function:")
for s in strings: # Print values in tuple
    print(f"    {s}")
    
print("   Concatenated string:", concatenation(s)) # Print concatenation

input("\n Press Enter to Continue...")
print_header("Task 2")

class Animal:
    """A simple class to list species and their names."""
    def __init__(self, **animal):
        """
        Initiate Animals class, takes any number of keyword arguments
        
        Seperate keywords for name and species
        """
        
        self.name = animal.get("name", "unknown")
        self.species = animal.get("species", "unknown")
        
    def speak(self):
        """Prints the animals and their names."""
        print(f"  {self.name} : {self.species}")
            
            
class Dog(Animal):
    """
    Creates a simple class to model dogs breed and color.
    
    Seperate arguments for breed and color
    """
    def __init__(self, *args, **animal):
        super().__init__(**animal)
        
        self.breed = animal.get("breed", "unknown") # Assign args to attribute
        self.color = animal.get("color", "unknown")
        
    def bark(self):
        """Returns woof!"""
        return "Woof!"
    
class Cat(Animal):
    """
    Creates a simple class to model cats breed and color.
    
    Seperate arguments for breed and color
    """
    def __init__(self, *args, **animal):
        super().__init__(**animal)
        
        self.breed = animal.get("breed", "unknown") # Assign args to attribute
        self.color = animal.get("color", "unknown")
        
    def meow(self):
        """Returns Meow!"""
        return "Meow!"
            
animal = Animal( # Create and instance of the Animal class
    name = "Turt",
    species = "Turtle"
)
animal.speak() # Call speak

print() # Spacer

dog = Dog( # Create an instance of the Dog class
    name = "Fipps",
    species = "Dog",
    breed = "Jack Russel",
    color = "White"
)
# Print details about animal
dog.speak() 
print(" ", dog.bark())

print() # Spacer

cat = Cat( # create an instance of the Cat class
    name = "Tiger",
    species = "Cat",
    breed = "Cat",
    color = "Black"
)
# Print details about animal
cat.speak()
print(" ", cat.meow())

print() # Spacer

def animal_speak(*animals):
    """Calls the speak method on each class bassed through"""
    print("  Animals")
    for animal in animals:
        animal.speak() # Call speak
        
# Call animal speak passing in previously made classes
animal_speak(animal, dog, cat)

input("\n Press Enter to Continue...")



    
        