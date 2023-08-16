# Zachary Hoover || 8-16-23 || Python 1 Review: Tuples

def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Step 1: Creating Tuples from User Input")

# get user information
student_name = input("  What is your name?: ").title()
student_age = input("  What is your age?: ")
student_favorite_subject = input("  What is your favorite subject?: ").title()

# Create tuple with information
student = (student_name, student_age, student_favorite_subject)

# Print tuple
print(f"\n  Student tuple: {student}")

# Create tuple with teacher information 
teacher_info = ("Brandon Dolce", 2414, "Python")

input("\n Press Enter to Continue...")
print_header("Step 2: Slicing Tuples")

# Seperate tuple into variables
teacher_name = teacher_info[0]
teacher_room = teacher_info[1]
teacher_subject = teacher_info[2]

# Print variables
print(f"  Teacher name: {teacher_name}")
print(f"  Teacher room: {teacher_room}")
print(f"  Teacher subject: {teacher_subject}")

print(f"\n  Teacher info: {teacher_info}")

input("\n Press Enter to Continue...")
print_header("Step 3: Using Tuples in Functions")

def print_teacher_info (teacher_information):
    """Prints teacher information."""

    # Print information from index
    print(f"  Teacher name: {teacher_information[0]}")
    print(f"  Teacher room: {teacher_information[1]}")
    print(f"  Teacher subject: {teacher_information[2]}")

    return
# Call function
print_teacher_info(teacher_info)

input("\n Press Enter to Continue...")






