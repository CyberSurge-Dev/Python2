# Zachary Hoover || 10-16-23 || Guided Practice #24

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

print_header("ASCII")

print(ord('A')) # Output: 65
print(chr(65)) # Output: A

input("\n Press Enter to Continue...")
print_header("UNICODE")

print('\u2764')
print(ord("❤")) # Output 10084

s = "මේ සිහල"
utf8_bytes = s.encode('utf-8')
print(utf8_bytes)

utf8_str = utf8_bytes.decode("utf-8")
print(utf8_str)

input("\n Press Enter to Continue...")
print_header("Code Points")

print(ord('A'))

print() # Spacer

# Convert a code point back into a character
print(chr(65))

input("\n Press Enter to Continue...")
print_header("ASCII Code Point")

print(ord('A')) # 65

input("\n Press Enter to Continue...")
print_header("UNICODE code point")

print(ord("❤"))

input("\n Press Enter to Continue...")
print_header("More than 1 code point")

print(ord("\U0001F60D")) # 128525

input("\n Press Enter to Continue...")
print_header("ASCII Converted Back")

print(chr(65))

input("\n Press Enter to Continue...")
print_header("UNICODE Converted Back")

print(chr(10084))

input("\n Press Enter to Continue...")
print_header("Code Point Converted Back")

print(chr(128525))

input("\n Press Enter to Continue...")
print_header("Addition")

num1 = '5'
num2 = '6'
sm = chr(ord(num1) + ord(num2))
print("The sum of", num1, "and", num2, "is", sm)

input("\n Press Enter to Continue...")
print_header("Subtraction")

num1 = '6'
num2 = '4'
diff = chr(ord(num1) - ord(num2))
print("The diference between", num1, "and", num2, "is", diff)

input("\n Press Enter to Continue...")
print_header("Multiplication")

num1 = '4'
num2 = '5'
prod = chr(ord(num1) * ord(num2))
print("The product of", num1, "and", num2, "is", prod)

input("\n Press Enter to Continue...")
print_header("Division")

num1 = '1'
num2 = '2'
quot = chr(ord(num1) // ord(num2))
print("The quotient of", num1, "and", num2, "is", quot)

input("\n Press Enter to Continue...")
print_header("ord()")

string = "Have a cutesie day!"
for char in string:
    code = ord(char)
    print(char, "has the ASCII code", code)
    
input("\n Press Enter to Continue...")
print_header("chr()")

codes = [72, 101, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
for code in codes:
    char = chr(code)
    print("The ASCII code", code, "corresponds to the character", char)
    
input("\n Press Enter to Continue...")
print_header(".isxxx")

string1 = "HELLO WORLD"
print(string1.isupper())

string2 = "123"
print(string2.isnumeric())

input("\n Press Enter to Continue...")
print_header(".join()")

my_list = ["apple", "bannana", "orange"]
result = ", ".join(my_list)

print(result)

input("\n Press Enter to Continue...")
print_header(".split()")

my_string = "Hello world, how are you?"
result = my_string.split()

print(result)

my_string = "apple, bannana, orange"
result = my_string.split(", ")

print(result)

input("\n Press Enter to Continue...")
print_header(".sort()")

my_list = ['apple', 'banana', 'orange']
my_list.sort()

print(my_list)

input("\n Press Enter to Continue...")
print_header("sorted()")

my_list = ['apple', 'banana', 'orange']
result = sorted(my_list)

print(result)

input("\n Press Enter to Continue...")
print_header(".index()")

my_string = "Hello world"

result = my_string.index("world")

print(result)

input("\n Press Enter to Continue...")
print_header(".find()")

my_string = "Hello World"
result = my_string.find("world")

print(result)

input("\n Press Enter to Continue...")
print_header(".rfind()")

my_string = "Hello world, welcome to Python"
index = my_string.rfind("o")
print(index)

input("\n Press Enter to Continue...")