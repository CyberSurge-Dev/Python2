# Zachary Hoover || 9-21-23 || Independent Practice #15

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

# Imports
import os
import math
import time
import random

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
    "Who holds the record for winning the most Oscars?":"walt disney"
}

num_questions = len(list(questions.keys()))
used_questions = [] # List of question that were already asked

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
            break
        else:
            clear()
            print_header("Trivia")
            print("  Incorrect!\n")
            attempts += 1

    used_questions.append(question)

input("\n Press Enter to Continue...")