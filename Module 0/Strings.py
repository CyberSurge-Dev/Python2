# Zachary Hoover || 8-15-23 || Python 1 Review: Strings

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("1. String Slicing")

# Create a string variable, slice variable
s = "PythonIsFun"
print(f"  {s[:6]} is from string: {s}")
print(f"  {s[8:]} is from string: {s}")

input("\n Press Enter to Continue...")
print_header("2. List/Array Slicing")

# Create a list, slice the list
lst = [0, 1, 2, 3, 4, 5]
print(f"  Items {lst[1:4]} are from list: {lst}")
print(f"  Items {lst[4:]} are from list: {lst}")

input("\n Press Enter to Continue...")
print_header("3. Using len()")

# Print the length of the string and list
print(f"  The length of {s} is {len(s)}")
print(f"  The length of {lst} is {len(lst)}")

input("\n Press Enter to Continue...")
print_header("4. Using count()")

# Count how many times 'n' appears in the string
print(f"  The letter 'n' appears {s.count('n')} times in {s}")

input("\n Press Enter to Continue...")
print_header("5. Using find()")

# Get index of first appearance of 'o' in the string
print(f"  The first 'o' in {s} is located at index {s.find('o')}")
# Check if 'z' is in the string
print(f"  Is 'z' in string {s} (-1 for no): {s.find('z')}")

input("\n Press Enter to Continue...")
print_header("6. String Formatters")

#Use string formaters to print a sentence
print("{0} {1} {2} {3} {4} {5}".format("I", "love", "programming", "in", "Python", 3))
print(f"{'I'} {'love'} {'programming'} {'in'} {'Python'} {3}")

input("\n Press Enter to Continue...")