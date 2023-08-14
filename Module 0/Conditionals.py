# Zachary Hoover || 8-14-23 || Python 1 Review: Condionals

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Exercise 1: Check if two numbers are different.")

def are_different(num1, num2):
    """Compares 2 numbers."""
    if num1 == num2:
        return False
    else:
        return True

num1 = int(input("  Enter a number: "))
num2 = int(input("  Enter another number: "))

print(f"  Are {str(num1)} and {str(num2)} different?", are_different(num1, num2))

input("\n Press Enter to Continue...")
print_header("Exercise 2: Find the largest number among three numbers.")

def find_largest(num1, num2, num3):
    """Finds the largest number in given list."""
    nums = []
    nums.extend([num1, num2, num3])

    nums.sort(reverse=True)

    return nums[0]

num1 = int(input("  Enter a number: "))
num2 = int(input("  Enter another number: "))
num3 = int(input("  Enter another number: "))

print("  The largest number entered is:", find_largest(num1, num2, num3))

input("\n Press Enter to Continue...")
print_header("Exercise 3: Using and, or in If Statements")

def in_range(num, start, end):
    """Checks if a number is in a given range."""
    if (num >= start) and (num <= end):
        return True
    else:
        return False

num1 = int(input("  Enter a number: "))
num2 = int(input("  Enter start of range: "))
num3 = int(input("  Enter end of range: "))

print("  Is", num1, "in range of", num2, "and", num3, "?", in_range(num1, num2, num3))

input("\n Press Enter to Continue...")
print_header("Exercise 4: Write a Python function age_group that categorizes ages.")

def age_checker(age):
    """Checks age ranges for given age."""
    if in_range(age, 0, 12):
        return "Child"
    elif in_range(age, 13, 19):
        return "Teenager"
    elif in_range(age, 20, 64):
        return "Adult"
    else:
        return "Senior"
        
age = int(input("  What is your age?: "))
print("  You are a", age_checker(age))

input("\n Press Enter to Continue...")
print_header("Exercise 5: Write a Python function can_drive that checks eligibility to drive based on age and vision.")

def can_drive(age, vision_score):
    """Checks if user is able to drive."""
    if (age >= 18) and (vision_score >= 0.8):
        return True
    else:
        return False

vScore = float(input("  What is your vision score?: "))
print("  Are you able to drive?", can_drive(age, vScore))

input("\n Press Enter to Continue...")






