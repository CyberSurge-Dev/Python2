# Zachary Hoover || 9-28-23 || Mini Project: Modules (A)

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os
import math
import time

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
clear()

print_header("Trivia")

def randRange(min_val, max_val):
    # Get the current system time in microseconds
    current_time = int(time.time() * 1e6)
    # Use the fractional part of the current time to generate randomness
    rand_fraction = (current_time % 1000000) / 1000000
    # Map the random fraction to the desired range of integers
    random_int = min_val + math.floor(rand_fraction * (max_val - min_val + 1))

    return random_int # return number

# Create a dictionary of trivia questions and answers
questions = {
    "Which actor voiced both Darth Vader and The Lion King's Mufasa?":"james earl jones",
    "How many Harry Potter books are there?":"7",
    "Which Avenger other than Captain America was able to pick up Thor's Mjolnir in the Marvel movies?":"vision",
    "Who wrote the Twilight books?":"stephenie meyer",
    "Who holds the record for winning the most Oscars?":"walt disney",
    "What day do Star Wars fans celebrate 'National Star Wars Day'?":"may 4th",
    "Who performed at the 2013 Super Bowl XLVII halftime show?":"beyonce",
    "Kaia Gerber is the daughter of what famous supermodel?":"cidny crawford",
    "Who directed the 1997 film, Titanic?":"james cameron",
    "What high school subject did Walter White teach on Breaking Bad?":"chemistry",
    "What A-list actor reprised his lead role as Maverick in the 2022 Top Gun sequel?":"tom cruise",
    "How many movies are there in the Halloween film franchise?":"13"
}

num_questions = len(list(questions.keys()))
used_questions = [] # List of question that were already asked

# Variable for the ammount the user got correct on the first attempt
correct = 0
# List to store incorrect questions
incorrect = []

for q in range(0, num_questions):
    while True: # Cycle through to choose a random, distinct question
        question = list(questions.keys())[randRange(0, num_questions-1)]
        if question not in used_questions:
            break
            
    attempts = 0 # Store the ammount of attempts taken
    
    while True: # Cylce through 
        print("  Attempts:", attempts)
        print(" ", question)
        answer = input("\n  Answer here: ")

        if answer.lower() == questions[question]:
            clear()
            print_header("Trivia")
            print("  Correct!\n")
            # If it's the first attempt, add 1 to correct
            if attempts < 1:
                correct += 1
            break
        else:
            clear()
            print_header("Trivia")
            print("  Incorrect!\n")
            attempts += 1
            if attempts > 2:
                break
            # Check if incorrect on first attempt
            elif attempts < 2:
                # Append question and answer to list
                incorrect.append((question, questions[question]))
            
            

    used_questions.append(question)
    
# Clear the screen
clear()
print_header("Trivia")

print(f"  Ammount correct (first attempt): {correct}")
print(f"\n  Incorrect questions:")
# Print each incorrect question, and the answer
for q, a in incorrect:
    print(f"    {q} : {a}")

input("\n Press Enter to Continue...")
