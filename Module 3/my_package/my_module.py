def my_function():
    print("  Hello, World!")
    
def add_numbers(a, b):
    return a + b

# code here will run when module is imported
print("  Module imported")

if __name__ == "__main__":
    # This code runs when the module is run as the main program
    result = add_numbers(2+3)
    print(result)
    