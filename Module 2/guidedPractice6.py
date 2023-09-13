# Zachary Hoover || 8-30-23 || Guided Practice #6

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

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
        
# creat an object from the class
my_new_car = Car('audi', 'a4', 2023)
# Print descriptive name using method
print(" ", my_new_car.get_descriptive_name())

input("\n Press Enter to Continue...")
print_header("Class Instances")

class MyClass:
    pass

class MySubclass(MyClass):
    pass

# Create class instances
obj1 = MyClass()
obj2 = MySubclass()

print("  obj1 instance of MyClass:", isinstance(obj1, MyClass)) # True
print("  obj2 instance of MyClass:", isinstance(obj2, MyClass)) # True
print("\n  obj1 instance of MySubclass: ", isinstance(obj1, MySubclass)) # False
print("  obj2 instance of MySubclass: ", isinstance(obj2, MySubclass)) # True

# Create variables of several types
x = 5
y = "hello"
z = [1, 2, 3]

# Print if they are instances
print(f"\n  {x} an instance of int?:", isinstance(x, int)) # True
print(f"  {y} an instance of str?:", isinstance(y, str)) # True
print(f"  {z} an instance of list, str?:", isinstance(z, (list, str))) # True

# isinstance() can be used to determine if a variable is a certain type

input("\n Press Enter to Continue...")
print_header("Setting Default Values")

# Create new Car onject
my_new_car = Car('audi', 'a4', 2023)
print(" ", my_new_car.get_descriptive_name())
# Read the odometer
my_new_car.read_odometer()

input("\n Press Enter to Continue...")
print_header("Modifying Attributes")

my_new_car = Car('audi', 'a4', 2023)
print(" ", my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()

# Update odometer
print("  After using my_new_car.update_odometer(23):")
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Print update
print("\n  After using my_new_car.update_odometer(20):")
my_new_car.update_odometer(20)

input("\n Press Enter to Continue...")
print_header("Incrementing an Attributes Value")

# Create and print a used car object
my_used_car = Car('subaru', 'outback', 2022)
print(" ", my_used_car.get_descriptive_name())

# '_' is in place of a comma 
my_used_car.update_odometer(23_500)
print("\n  Miles on car at purchase:")
my_used_car.read_odometer()

# Update miles and print
print("\n  Miles on car after 100 miles:")
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

input("\n Press Enter to Continue...")
print_header("Introspection")

class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"
        self.__private_var = "This is a private variable"
        
# Create instance of MyClass
obj1 = MyClass()
        
# Using hasattr to determine type of variable in class (publi and private)
print("  MyClass has attribute 'public_var':", hasattr(obj1, 'public_var'))
print("  MyClass has attribute '__private_var':", hasattr(obj1, '__private_var'))

input("\n Press Enter to Continue...")
print_header("__dict__ Introduction")

class MyClass:
    """This is a simple class for __dict__ testing."""
    class_var = "class value"
    
    def __init__(self):
        self.instance_var = "instance value"
        
# Create instance of MyClass to obj
obj = MyClass()
# See what is in obj
print("  obj.__dict__:", obj.__dict__)
print("\n  MyClass.__dict__:", MyClass.__dict__)

class MyClass:
    pass

# Create instance of MyClass to obj
obj = MyClass()

# Add a new variable to the class
obj.__dict__["new_attr"] = "new value"
# See what is in obj
print("\n  obj.__dict__:", obj.__dict__)

input("\n Press Enter to Continue...")
print_header("__dict__ Property")

class MyClass:
    """This is a simple class for __dict__ testing"""
    x = 5
    def __init__(self):
        self.y = 10
        
print("  MyClass.__dict__:", MyClass.__dict__)

input("\n Press Enter to Continue...")
print_header("__dict__ Introduction")

class MyClass:
    """This is a simple class for __dict__ testing"""
    def __init__(self):
        self.x = 5
        self.y = 10
        
obj = MyClass()
print("\n  obj.__dict__:", obj.__dict__)

class MyClass:
    """This is a simple class for __dict__ testing"""
    x = 5
    
    def __init__(self):
        self.y = 10
        
print("\n  MyClass.__dict__:", MyClass.__dict__)
# MyClass.__dict__['x'] = 10
print(" ", MyClass.x)

obj = MyClass()
print("\n  obj.__dict__:", obj.__dict__)
obj.__dict__['y'] =20
print(" ", obj.y)

input("\n Press Enter to Continue...")
print_header("Private Components")

class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"
        self.__private_var = "This is a private variable"
        
    def get_private_var(self):
        return self.__private_var
    
obj = MyClass()

print(" ", obj.public_var)
print(" ", obj.__private_var)

print()

class MyClass:
    def __init__(self):
        self.public_var = "This is a public variable"
        
    def __private_method(self):
        print("  This is a private method")
        
    def public_method(self):
        print("  This is a public method")
        self.__private_method()
    
obj = MyClass()

# Call methods
obj.public_method()
obj.__private_method()

input("\n Press Enter to Continue...")