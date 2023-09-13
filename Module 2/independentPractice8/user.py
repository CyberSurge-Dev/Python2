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