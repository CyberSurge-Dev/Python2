# Zachary Hoover || 10-24-23 || Independent Practice #27

# Imports
import os
import string
import sys

# Code to clear the screen before running
clear = lambda: os.system('clear' if os.name == 'posix' else 'cls')
# Store the path of the folder that this file is stored in
path = __file__[:len(__file__.rpartition('\\')[0])]
# Create a filename variable to store the filepath
filename = os.path.join(path, "students.txt")

def print_header(title):
    """Prints header with title."""
    clear()
    print("\n ------+ " + title + " +------\n")
    return

# --+ Program Starts Here +----------------------------------------------------

class Student():
    """Student class to store details about student"""
    def __init__(self, student_id, first_name, last_name, email, gpa):
        """Initialize variables for class"""
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gpa = gpa

    def info(self):
        """Returns a formated string with information about the object"""
        return(f"""  student_id: {self.student_id}
  name: {self.first_name} {self.last_name}
  email: {self.email}
  gpa: {self.gpa}""")

    def __str__(self):
        """Returns information about the object in the form of a string."""
        return f"{self.student_id}, {self.first_name}, {self.last_name}, {self.email}, {self.gpa}"

def read_students_from_file(filename):
    """Reads students from the provided filename, returns a list of Student objects."""
    students = [] # Create an empty list to store return student objects

    try:
        # Store each line of the file in a list
        with open(filename, 'r') as file:
            lines = file.read().split('\n')[:-1]
    except FileNotFoundError:
        # Print an error message and return an empty list
        print(f"Error: File {filename} does not exist.")
        return []
        

    # Seperate lines into list
    # lines = lines.split('\n')
    # Cycle through each line in the file andcreate an object based on that
    for line in lines:
        # Remove whitespace and split the string were the commas are into the data
        details = line.replace(" ", "").split(',') # Allows for any ammount of space between items on the same line
        
        try:
            # Check to make sure the length is correct for all data
            if len(details) != 5:
                raise ValueError("Missing information")

            students.append(Student(
                student_id= details[0],
                first_name= details[1],
                last_name= details[2],
                email= details[3],
                gpa = float(details[4]) # If the conversion fails, this will raise a value error
            ))
        except ValueError:
            # Print an error message and return an empty list
            print(f"Error: Information at line {lines.index(line)+1} in {filename} is not correct.")
            return []

    return students

def write_students_to_file(students, filename):
    """Writes the given student objects to the file provided"""
    # Open the file
    try:
        with open(filename, "a") as file:
            # Cycle through and write each student to the file
            for student in students:
                # Check to make sure information is a student object
                if type(student) != Student:
                    raise ValueError("All objects must be Student objects.")
                # Write the student to the file (__str__ string)
                file.write(student.__str__() + "\n")

    except FileNotFoundError:
        print("Error: File was not found.")
    except ValueError as ve:
        print(ve)

def multi_type_input(labels, types):
    """
    labels, types
    
    takes in tuple or list of types and list f labels, allows the user to enter values each 
    time and checks if the value is the correct type, if it's not, prints
    a message and allows for the information to re-entered

    Returns a tuple of filtered inputs
    """
    # List for output values
    outputs = []

    if len(labels) != len(types):
        raise ValueError("Length of labels and types is not equal.")

    # Loop through each type
    for i in range(0, len(labels)):
        # Loop through until valid input
        while True:
            # get user input 
            inp = input(labels[i])

            try:
                # Check for types
                if inp == "": return None
                elif types[i] == string: inp = inp.replace(' ', ''); break # Remove anything after a space
                elif types[i] == float: inp = float(inp); break
                elif types[i] == int: inp = int(inp); break
                else: raise ValueError(f"{type} is not a valid type.")
            except ValueError as ve:
                print(ve)
        outputs.append(inp)

    return tuple(outputs)

def main():
    """
    The mian function fro the program, has the menu for adding and reading students
    Calling the function several times within itself is usually not
    best practice, but it is done here to make the code easier to read.

    Additionally, this program uses Excessive error handling in nearly every aspect.
    Because of this, you should be able to change anything about the file,
    and enter whatever you would like and it should be accounted for.
    """
    global filename
    # Print menu for user
    print_header("Student Explorer")
    print("  1. Add Student")
    print("  2. Add Multiple Students")
    print("  3. Read Students")
    print("  4. Change File")
    print("  5. Exit")

    user_input = input("\n Enter selected item (1-5): ")

    # Check inputs and choose mode
    if user_input == "1":
        # Clear scren
        print_header("Student Explorer")
        # Use multi_type_input to get inputs
        inputs = multi_type_input((
            "Enter student id: ",
            "Enter student's first name: ",
            "Enter student's last name: ",
            "Enter student's email: ",
            "Enter student's GPA: "
        ),(string, string, string, string, float))
        
        # If user cancels, return to main
        if inputs == None:
            main()

        print(inputs)

        # Append student to file
        write_students_to_file([Student(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])], filename)
        # Return to main
        main()

    if user_input == "2":
        # Create list to hold students
        students = []
        # loop through until user wants to quit
        while True:
            # Clear scren
            print_header("Student Explorer")
            # Use multi_type_input to get inputs
            inputs = multi_type_input((
                "Enter student id: ",
                "Enter student's first name: ",
                "Enter student's last name: ",
                "Enter student's email: ",
                "Enter student's GPA: "
            ),(string, string, string, string, float))

            # Append student to list
            students.append(Student(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]))

            # Check if user wants to quit
            inp = input("Do you want to add another (y/n)?: ")
            if inp.lower() == 'n':
                break
                
        # Add students to file
        write_students_to_file(students, filename)
        # Return to main
        main()

    elif user_input == "3":
        # Read the file and store in variable
        students = read_students_from_file(filename)

        # Print students to console
        print(f"Students from {filename}: ")
        for student in students:
            print(student.info()+"\n")

        input("\n Press Enter to Continue...")
        main() # Return to menu

    elif user_input == "4":
        # Clear scren
        print_header("Student Explorer")
        # Print current
        print(f"Current path:\n{filename}")
        # Get new path
        new_path = input("\nEnter new path (press enter to cancel): ")
        # Check for cancel
        if new_path != "":
            filename = new_path
        
        # Return to main
        main()

    elif user_input == "5":
        sys.exit()
        
    else:
        # Return to main
        main()

# Run main on startup
main()