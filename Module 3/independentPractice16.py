# Zachary Hoover || 9-21-23 || Independent Practice #15

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

# Create a dictionary of trivia questions and answers
questions = {
    "Question 1":"",
    "Question 2":"",
    "Question 3":"",
    "Question 4":""
}

num_questions = len(list(questions.keys()))

# Using time, get a random index for questions
def getRandom():
    """Returns a number 0-4 based on the current time"""
    return 

input("\n Press Enter to Continue...")
print_header("Example 3");