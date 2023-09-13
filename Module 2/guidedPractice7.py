# Zachary Hoover || 9-5-23 || Guided Practice #6

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Example")
# Examples
class ParentClass:
    def __init__(self, x):
        self.x = x
    
class ChildClass(ParentClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        
class Person:
    def greet(self):
        print("  Hello!")
        
class Student(Person):
    def greet(self):
        super().greet()
        print("  Hi, i'm a student!")
        
s = Student()
s.greet()

input("\n Press Enter to Continue...")
print_header("Inheriting Attributes & Methods")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def speak(self):
        print(f"  {self.name} says {self.sound}.")
        
class Dog(Animal):
    pass

dog = Dog("Fido", "Woof")
dog.speak() # Fido says Woof.

input("\n Press Enter to Continue...")
print_header("Ovrriding Methods")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def speak(self):
        print(f"  {self.name} says {self.sound}.")
        
class Dog(Animal):
    def speak(self):
        print(f"  {self.name} barks.")
        
dog = Dog("Fido", "Woof")
dog.speak() # Fido says Woof.

input("\n Press Enter to Continue...")
print_header("Adding New Methods & Attributes")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def speak(self):
        print(f"  {self.name} says {self.sound}.")
        
class Dog(Animal):
    def bark(self):
        print(f"  {self.name} barks loudly.")
        
dog = Dog("Fido", "Woof")
dog.speak() # Fido says Woof.
dog.bark() # Fido barks loudly.

input("\n Press Enter to Continue...")
print_header("The Car Class")

class Car:
    """Simple model to represent a car."""
    
    def __init__(self, make, model, year):
        """Initizlize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formated descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}".title()
        
        return long_name
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"  This {self.get_descriptive_name()} has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the odometer.
        """
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("  You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Fill the gas tank."""
        print("  Filled the gas tank.")
        
class Battery():
    """A simpe model for an electric car battery"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attribute"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"  This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print statement about the range in miles on a full charge"""
        if self.battery_size ==75:
            r = 260
        elif self.battery_size == 100:
            r = 315
            
        print(f"  This car can go about {r} miles on a full charge")
        
class ElectricCar(Car):
    """Represent assprects of a car, specific to electic vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        
        self.battery = Battery()
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        self.battery.describe_battery()
        
    def fill_gas_tank(self):
        """Electric cars don't use gas."""
        print("  Electric cars don't use gas.")
        
        
        
my_tesla = ElectricCar('tesla', 'model s', 2023)
print(" ", my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

input("\n Press Enter to Continue...")

