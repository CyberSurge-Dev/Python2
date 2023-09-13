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
        
