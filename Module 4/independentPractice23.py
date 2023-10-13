# Zachary Hoover || 10-12-23 || Independent Practice #23

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

print_header("Independent Practice #23")

class SongError(Exception):
    """Simple class for all song related errors (for simplicity later)"""
    pass

# Create a class (error) for each major genre of music
class PopError(SongError):
    """Class for PopError, triggers an Exception."""
    def __init__(self, title, artist):
        """Initializes class, triggers exception"""
        self.title = title
        self.artist = artist
        super().__init__(f"Error: {title} by {artist} is a Pop song.")
    
class RockError(SongError):
    """Class for RockError, triggers an Exception."""
    def __init__(self, title, artist):
        """Initializes class, triggers exception"""
        self.title = title
        self.artist = artist
        super().__init__(f"Error: {title} by {artist} is a Rock song.")
        
class HipHopError(SongError):
    """Class for HipHopError, triggers an Exception."""
    def __init__(self, title, artist):
        """Initializes class, triggers exception"""
        self.title = title
        self.artist = artist
        super().__init__(f"Error: {title} by {artist} is a Hip-Hop song.")
        
class CountryError(SongError):
    """Class for CountryError, triggers an Exception."""
    def __init__(self, title, artist):
        """Initializes class, triggers exception"""
        self.title = title
        self.artist = artist
        super().__init__(f"Error: {title} by {artist} is a Country song.")

def check_song(song):
    """Checks a list of dictionaries passed in for specific keywords and displays an error if found."""
    try:
        # Check to make sure the dictionary has song attributes    
        assert song.get('genre', None) != None and song.get('title', None) != None and song.get('artist', None) != None, "Song is not valid."
        
        # Check if the song is any forbidden genre, if it is, trigger an error
        if song['genre'] == 'pop':
            raise PopError(song['title'], song['artist'])
        elif song['genre'] == 'hip-hop':
            raise HipHopError(song['title'], song['artist'])
        elif song['genre'] == 'rock':
            raise RockError(song['title'], song['artist'])
        elif song['genre'] == 'country':
            raise CountryError(song['title'], song['artist'])
        
    except AssertionError as a:
        # Raise an error if a song is passed in that is not valid
        raise ValueError(a)
    
    # Return a message if the song is valid
    return f"Now playing: {song['title']} by {song['artist']}"

# Create a list of dictionaries that store the details about each song
playlist = [
    {"title":"Crazy", "artist":"Gnarls Barkley", "genre":"pop"},
    {"title":"Bohemian Rhapsody", "artist":"Queen", "genre":"rock"},
    {"title":"Friends in Low Places", "artist":"Garth Brooks", "genre":"country"},
    {"title":"It Was a Good Day", "artist":"Ice Cube", "genre":"hip-hop"},
    {"title":"What a Wonderful World", "artist":"Louis Armstrong", "genre":"jazz"}
    
]

# Cylce through the songs in the playlist
for song in playlist:
    # Try checking the song
    try:
        print(check_song(song))
    except SongError as se:
        # Print any song related errors
        print(se)

input("\n Press Enter to Continue...")
