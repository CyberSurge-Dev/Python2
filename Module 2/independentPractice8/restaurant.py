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