# Zachary Hoover || 8-29-23 || Independent Practice #5

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Restaurant")

class Restaurant:
    """Simple model for a restaurant attributes"""
    
    def __init__(self, name, cuisine_type):
        """Initizlize restaurant with name and cuisine type"""
        
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Prints a few lines that describes the restaurant"""
        
        print(f"  The restaurants name is: {self.restaurant_name}")
        print(f"  The restaurants cuisine type is: {self.cuisine_type}")
        
    def open_restaurant(self):
        """Opens the restaurant and prints a message"""
        
        print(f"  {self.restaurant_name} is now open!")
        
# Initizlize restaurant 
restaurant = Restaurant('Taco Bell', 'Mexican')

restaurant.describe_restaurant()
print("")
restaurant.open_restaurant()

input("\n Press Enter to Continue...")
print_header("Three Restaurants")

class Restaurant:
    """Simple model for a restaurant attributes"""
    
    def __init__(self, name, cuisine_type):
        """Initizlize restaurant with name and cuisine type"""
        
        self.restaurant_name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Prints a few lines that describes the restaurant"""
        
        print(f"  The restaurants name is: {self.restaurant_name}")
        print(f"  The restaurants cuisine type is: {self.cuisine_type}")
        
    def open_restaurant(self):
        """Opens the restaurant and prints a message"""
        
        print(f"  {self.restaurant_name} is now open!")
        
# Initizlize restaurant 0
restaurant0 = Restaurant('Taco Bell', 'Mexican')
# Call methods from restaurant0
restaurant0.describe_restaurant()
restaurant0.open_restaurant()

# Print for spacing
print()

# Initizlize restaurant1
restaurant1 = Restaurant('McDonalds', 'American')
# Call methods from restaurant1
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

# Print for spacing
print()

# Initizlize restaurant2
restaurant2 = Restaurant("Carrabba's", 'Italian')
# Call methods from restaurant2
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

input("\n Press Enter to Continue...")
print_header("Users")

class User:
    """Simple model for users and user information"""
    
    def __init__(self, first_name, 
                 last_name, 
                 username, 
                 age, 
                 email, 
                 password):
        """Initialize user, store information in variables for class"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.email = email
        self.password = password
        
    def describe_user(self ):
        """Prints details about the user"""
        
        print(f"  {self.first_name} {self.last_name}:")
        print(f"    Username: {self.username}")
        print(f"    age: {self.age}")
        print(f"\n    Email: {self.email}")
        print(f"    Password: {self.password}")
        
# Create user from class
user = User("Zachary",
            "Hoover",
            "zhoover2891",
            16,
            "zhoover2891@cabarrus.k12.nc.us",
            "1234567890")
# Call describe_user method to describe user
user.describe_user()
        
input("\n Press Enter to Continue...")