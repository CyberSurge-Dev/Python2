# Zachary Hoover || 10-30-23 || PCAP Practice #2

# Imports
import os

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])] + '\\'

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

class SocialMediaPost:
    """Class for modeling a social media post"""
    def __init__(self, username, content):
        """Initialize the post with variables"""
        self.username = username
        self.content = content
    
def create_post(username, content):
    """Creates a ost, handles errors"""
    # Check for empty inputs
    if username == "":
        raise ValueError("Username cannot be empty!")
    if content == "":
        raise ValueError("Content cannot be empty!")
    # Check for inputs that are too large
    elif len(content) > 280:
        raise ValueError("Content exceeds character limit!")
    
    return SocialMediaPost(username, content)

# Create a lists to store the posts
posts = []

# Loop through and create social media posts from user input
while True:
    try:
        # Get the input from the user
        print_header("Post Creator")
        posts.append(create_post(input("Enter your username: "), input("Enter post content: ")))
    except ValueError as ve:
        # catch and print exceptions
        print("\n" + str(ve))
        input("Press enter to try again...")
        continue
        
    # Ask the user for another input
    if input("\nDo you want to create another (y/n)?: ").lower() == 'n':
        break

# Print the posts
print_header("Post Creator")
for post in posts:
    print(post.username+":")
    print(" ", post.content+"\n")
        
input("\n Press Enter to Continue...")
