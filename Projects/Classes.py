# Zachary Hoover || Mini Project: Classes
# 9-14-23 

# Imports
import random

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Lottery")

class Lottery:
    """Simple class to model a lottery game"""
    def __init__(self):
        """Initialize class and ticket."""
        # Create list of numbers 1-10 and letters A-E
        self.pool = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']
                
    def draw(self):
        """Returns a tuple of 4 random selections from the pool attribute."""
        # Return a tuple of 4 random selections from pool
        return tuple([random.choice(self.pool) for i in range(0, 4)])
            
    def get_user_ticket(self):
        """Prompts the user for 4 seperate letters or numbrs and returns them as a tuple."""
        
        notValid = True
        while notValid: # create a loop for user to create ticket until a valid one is made
            # Get user input
            print("""  Enter 4 terms seperated by commas(,).
  These terms can be either a number 1-10, or a letter A-E
                  """)
            inp = input("  Enter Here: ") # get user input
            inp = inp.split(",") # Convert user input to list for validation
            
            if len(inp) < 4:
                print("  Not all terms were entered!\n")
                continue
            
            for i in range(0, len(inp)):
                if i >= 4:
                    break
                else:
                    # Check if the current term is valid
                    if inp[i].strip().upper() in self.pool:
                        # Format the term correctly
                        inp[i] = inp[i].strip().upper()
                    else:
                        print(f"  {inp[i].strip()} is not a valid term!\n")
                        break
                    
                    if (i == 3): # Check if this is the last term
                            notValid = False
                            break
        return tuple(inp[:5]) # Return the ticket (up to 4 terms)
                    
    def analyze_ticket(self, my_ticket):
        """Compares the given tupke(my_ticket) to new tickets and returns the count of tickets needed before winning."""
        count = 0 # Create a variable for count
        
        while True:
            if my_ticket == self.draw(): # generate new ticket and compare
                break 
            count += 1
        return count # return count
  
lottery = Lottery() # initialize the lottery class

# Let the user create a ticket
user_ticket = lottery.get_user_ticket()
# Draw a winner
draw_ticket = lottery.draw()

# Check if the ticket is a winner
if (user_ticket == draw_ticket):
    print("\n  You Win! :) \n")
else:
    print("\n  You Loose! :( \n")

# Print information about tickets
print(f"  Your ticket: {str(user_ticket)}")
print(f"  Winning ticket: {str(draw_ticket)}")

input("\n Press Enter to Continue...")
print_header("Lottery Analysis")

lottery = Lottery() # Initialize new lottery class

# Let the user create a ticket
user_ticket = lottery.get_user_ticket()

# Check how many draws it will take to get a winner using analyze ticket.
count = lottery.analyze_ticket(user_ticket) # get the count needed to win
    
# Print the count
print(f"\n  It took {count} draws to get a winning ticket.")

input("\n Press Enter to Continue...")

