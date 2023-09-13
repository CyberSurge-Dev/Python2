# Zachary Hoover || 9-7-23 || Guided Practice #8

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Importing a Single Class")

from car import Car

my_new_car = Car('audi', 'a4', 2023) # Create instance
print(" ", my_new_car.get_descriptive_name()) # Print descriptive name

input("\n Press Enter to Continue...")
print_header("Electric Car")

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2023) # Create instance of ElectricCar
print(" ", my_tesla.get_descriptive_name()) # Print descriptive name

# Print information about battery
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

input("\n Press Enter to Continue...")
print_header("Importing Multiple Classes From One Module")

from car import Car, ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2019) # Create instance
print(" ", my_beetle.get_descriptive_name()) # Print name

my_tesla = ElectricCar('tesla', 'roadster', 2021) # Create instance of ElectricCar
print(" ", my_tesla.get_descriptive_name()) # Print descriptive name

input("\n Press Enter to Continue...")
print_header("Module to Module")

from cars import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagon', 'beetle', 2019) # Create instance
print(" ", my_beetle.get_descriptive_name()) # Print name

my_tesla = ElectricCar('tesla', 'roadster', 2021) # Create instance of ElectricCar
print(" ", my_tesla.get_descriptive_name()) # Print descriptive name

input("\n Press Enter to Continue...")
print_header("Using Aliases")

from cars import Car
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2021) # Create instance of ElectricCar
print(" ", my_tesla.get_descriptive_name()) # Print descriptive name

input("\n Press Enter to Continue...")


