from cars import Car

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