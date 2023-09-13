from users import User

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