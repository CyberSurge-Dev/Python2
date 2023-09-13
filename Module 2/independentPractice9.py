# Zachary Hoover || 9-11-23 || Independent Practice #9

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Task 1")

class PowerRanger():
    """A simple model for a PowerRanger."""
    def display_power(self):
        return f"{self.color} Ranger, {self.power}!"
    
class RedRanger(PowerRanger):
    """Simple model for Red Power Ranger."""
    color = "Red"
    power = "Tyrannosaurus"
    
class BlueRanger(PowerRanger):
    """Simple model for Blue Power Ranger."""
    color = "Blue"
    power = "Triceratops"
    
class YellowRanger(PowerRanger):
    """Simple model for Yellow Power Ranger."""
    color = "Yellow"
    power = "Sabertooth Tiger"
    
class GreenRanger(PowerRanger):
    """Simple model for Green Power Ranger."""
    color = "Green"
    power = "Dragonzord"   
    
class BlackRanger(PowerRanger):
    """Simple model for Black Power Ranger."""
    color = "Black"
    power = "Mastodon"
    
class PinkRanger(PowerRanger):
    """Simple model for Pink Power Ranger."""
    color = "Pink"
    power = "Pterodactyl"
    
class WhiteRanger(PowerRanger):
    """Simple model for White Power Ranger."""
    color = "White"
    power = "Tigerzord"
    
# Create a tuple for all the colors of Power Ranger
powerRangers = (
    RedRanger(),
    BlueRanger(),
    YellowRanger(),
    GreenRanger(),
    BlackRanger(),
    PinkRanger(),
    WhiteRanger()
)

# Iterate through the power rangers and use polymorphism to display the power
for ranger in powerRangers:
    print(" ", ranger.display_power())
    
    
input("\n Press Enter to Continue...")
print_header("Task 2")

class Zord:
    """Simple class to model Zord"""
    def attack(self):
        """Simple method to print class' attack."""
        print("  Generic Zord attack!")
        
class TryannosaurusZord(Zord):
    """Simple class to model Tryannosaurus Zord"""
    def attack(self):
        """Simple method to print class' attack."""
        print("  Tyrannosaurus Zord, Tyranno Slash!")
        
class TriceratopsZord(Zord):
    """Simple class to model Triceratops Zord"""
    def attack(self):
        """Simple method to print class' attack."""
        print("  Triceratops Zord, Tricera Charge!")
    
# Create a tuple of all the Zord classes 
Zords = (
    Zord(),
    TryannosaurusZord(),
    TriceratopsZord()
)

# Itterate through the Zords tuple and print their attack
for zord in Zords:
    # call Zord's attack
    zord.attack()


input("\n Press Enter to Continue...")