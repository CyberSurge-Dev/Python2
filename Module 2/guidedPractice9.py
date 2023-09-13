# Zachary Hoover || 9-11-23 || Guided Practice #9

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Polymorphic Fishing Rangers")

class Shark():
    def swim(self):
        print("  The shark is swimming.")
    def swim_backwards(self):
        print("  The shark cannot swim backwards, but can sink backwards.")
        
    def skeleton(self):
        print("  The shark's skeleton is made of cartilage.")
        
class Clownfish():
    def swim(self):
        print("  The clownfish is swimming.")
    def swim_backwards(self):
        print("  The clownsih is swimming backwards.")
        
    def skeleton(self):
        print("  The clownfish's skeleton is made of bone.")
        
sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

input("\n Press Enter to Continue...")
print_header("Polymorphing: Dino Thunder")

sammy = Shark()
casey = Clownfish()

for fish in (sammy, casey):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()
    
input("\n Press Enter to Continue...")
print_header("Polymorphing: Wild Force")

def in_the_pacific(fish):
    fish.swim()
    
sammy = Shark()
casey = Clownfish()

in_the_pacific(sammy)
in_the_pacific(casey)

input("\n Press Enter to Continue...")