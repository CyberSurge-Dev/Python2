# Zachary Hoover || 8-29-23 || Independent Practice #5

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Task 1 - Number Served")

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

# Create instance
restaurant = Restaurant("restaurant", "food")

# Describe restaurant
restaurant.describe_restaurant()

# Change value of customers served
restaurant.set_number_served(22)
print(f"\n  Set number_served to {restaurant.number_served} \n")
# Describe restaurant
restaurant.describe_restaurant()

# Increment number_served by one
restaurant.increment_number_served()
print(f"\n  Incremented number_served by one \n")
# Describe restaurant
restaurant.describe_restaurant()


input("\n Press Enter to Continue...")
print_header("Task 2 - Login Attempts")

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
        
# create dictionary for users
users = {}
        
# Allow the user to create account(s)
while True:
    print("\n  Create Account")
    fn, ln = input("    Enter your first name and last name (Fn Ln): ").title().split()
    username = input("    Enter your username: ")
    password = input("    Enter your password: ")
    
    # Create instance of User class with details and add it to the dictionary through username
    users[username] = User(fn, ln, username, password) # add to users dictionary
    
    # Check if the user wants to create another account
    i = input("\n    Would you like to create another user? (y/n): ")
    if i.lower() == 'n' or i.lower() == 'no':
        break

# Allow user to login 
print("\n  Login")
while True:
    # get username
    username = input("    Username: ")
    
    # Check for username in user
    if (username not in users):
        print("    User not found!\n")
        # return to begining of loop
        continue
    else:
        # Allow user to enter password
        print() # spacer
        while True:
            # get password from user
            password = input("    Password: ")
            
            # Check if password is correct
            if (password != users[username].password):
                # Print message
                print("    Password incorrect!")
                
                # Increment attempts
                users[username].increment_login_attempts()
                print(f"    Attempts: {users[username].login_attempts}\n")
                continue
            else:
                # Print welcome message
                print(f"\n  Welcome, {users[username].first_name} {users[username].last_name}!")
                break
    break

print("\n  Attempts reset.") # Spacer
# Reset login attempts
users[username].reset_login_attempts()
# Print user details
users[username].describe_user()

input("\n Press Enter to Continue...")