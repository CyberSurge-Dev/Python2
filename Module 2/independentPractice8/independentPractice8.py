# Zachary Hoover || 9-5-23 || Independent Practice #7

def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Imported Restaurant")

# Imports
from restaurant import Restaurant

# create an instance of restaurant
restaurant = Restaurant("carabba's", "italian")
# Describe the restaurant
restaurant.describe_restaurant()

input("\n Press Enter to Continue...")
print_header("Imported Admin")

# Imports
from user import Admin

# Create instance of Admin
admin = Admin("Zachary", "Hoover", "zhoover2891", "1234", [
    "add-posts",
    "delete-posts",
    "ban-users",
    "edit-posts",
    "edit-users"
])

admin.describe_user() # describe the admin
print() # Spacer
admin.privileges.show() # Display privileges

input("\n Press Enter to Continue...")
print_header("Multiple Modules")

# Imports
from privileges import Admin as Admin2

# Create instance of Admin
admin = Admin2("Zachary", "Hoover", "zhoover2891", "1234", [
    "add-posts",
    "delete-posts",
    "ban-users",
    "edit-posts",
    "edit-users"
])

admin.describe_user() # describe the admin
print() # Spacer
admin.privileges.show() # Display privileges

input("\n Press Enter to Continue...")