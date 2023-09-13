# Zachary Hoover || 9-5-23 || Independent Practice #7

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Ice Cream Stand")

class Restaurant:
    """Simple model for a restaurant attributes."""
    
    def __init__(self, name, cuisine_type):
        """Initizlize restaurant with name and cuisine type."""
        
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Prints a few lines that describes the restaurant."""
        
        res = self.restaurant_name.title()
        
        print(f"  The restaurants name is: {res}")
        print(f"  {res}'s cuisine is: {self.cuisine_type}")
        print(f"  {res} has served {self.number_served} customers")
        
    def open_restaurant(self):
        """Opens the restaurant and prints a message."""
        
        print(f"  {self.restaurant_name} is now open!")
        
    def set_number_served(self, number):
        """Sets the number of customer served to given value."""
        
        self.number_served = number
        
    def increment_number_served(self):
        """Increments the number served by 1."""
        
        self.number_served += 1
        
class IceCreamStand(Restaurant):
    """Simple model for an icecream stand."""
    def __init__(self, name, flavors):
        """Initialize attributes for IceCreamClass"""
        super().__init__(name, "ice cream")
        
        self.flavors = flavors
        
    def display_flavors(self):
        """Prints the list of flavors at the ice cream stand"""
        print(f"  Flavors at {self.restaurant_name}:")
        # Print flavors
        for flavor in self.flavors:
            print(f"    {flavor}")
        
# Create instance of IceCreamStand
stand = IceCreamStand("Kool Icecream", [
    "chocolate", 
    "vanilla", 
    "strawberry", 
    "rocky road", 
    "caramel", 
    "peanut butter cups", 
    "oreo"
])

stand.describe_restaurant() # Describe the restaurant
print() # Spacer
stand.display_flavors() # Print flavors

input("\n Press Enter to Continue...")
print_header("Admin & Privileges")

class User:
    """Simple model for users and user information"""
    
    def __init__(self, first_name, 
                 last_name, 
                 username, 
                 password):
        """Initialize user, store information in variables for class"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.login_attempts = 0
        
    def describe_user(self ):
        """Prints details about the user"""
        
        print(f"  {self.first_name} {self.last_name}:")
        print(f"    Username: {self.username}")
        print(f"    Password: {self.password}")
        print(f"    Login attempts: {self.login_attempts}")
        
    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """Resets the value of login_attempts back to zero"""
        
        self.login_attempts = 0
        
class Privileges:
    """Simple model for privileges"""
    def __init__(self, privileges):
        """Initialize privileges"""
        self.privileges = privileges
        
    def show(self):
        print(f"  Privileges:")
        # Print flavors
        for perm in self.privileges:
            print(f"    {perm}")
            
class Admin(User):
    """Simple model for an admin user."""
    def __init__(self, first_name, last_name, username, password, privileges):
        super().__init__(first_name, last_name, username, password)
        
        self.privileges = Privileges(privileges)
        
    # Def show_privileges(self):
    #   print(f"  {self.username}'s Privileges:")
    #   for perm in self.privileges:
    #       print(f"    {perm}")
            
admin = Admin("Zachary", "Hoover", "zhoover2891", "1234", [
    "add-posts",
    "delete-posts",
    "ban-users",
    "edit-posts",
    "edit-users"
])

admin.describe_user() # describe the admin
print() # Spacer
admin.privileges.show() # Display privileges

input("\n Press Enter to Continue...")
print_header("Battery Upgrade")

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
        
    def upgrade_battery(self):
        """Upgrades the battery to 100kWh if it is not already."""
        if self.battery_size == 75:
            # Upgrade battery
            self.battery_size = 100
            # print message
            print("  The battery has been upgraded to 100 kWh")
        elif self.battery_size == 100:
            # print message
            print("  The battery in this car has already been upgraded.")
        else:
            # Print message
            print("  This car is not elgible for a battery upgrade.")
            
        
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
        
my_tesla = ElectricCar('tesla', 'model s', 2023) # Create instence
print(" ", my_tesla.get_descriptive_name()) 
my_tesla.battery.describe_battery() # Describe the battery
my_tesla.battery.get_range() # Get the range
print() # spacer
my_tesla.battery.upgrade_battery() # upgrade the battery
my_tesla.battery.describe_battery() # Describe the battery
my_tesla.battery.get_range() # Get the range
print() # spacer
my_tesla.battery.upgrade_battery() # upgrade the battery
my_tesla.battery.describe_battery() # Describe the battery
my_tesla.battery.get_range() # Get the range

input("\n Press Enter to Continue...")

            
