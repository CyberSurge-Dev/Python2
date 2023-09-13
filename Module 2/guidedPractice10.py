# Zachary Hoover || 9-12-23 || Guided Practice #10

from re import L


def print_header(title):
    """Prints header with title"""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Understanding Args")

def multiply(x, y):
    print(" ", x * y)
    
multiply(5, 4)
# multiply(5, 4, 3)

input("\n Press Enter to Continue...")
print_header("Let's try not to error!")

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(" ", z)
    
multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)

input("\n Press Enter to Continue...")
print_header("Understanding **kwargs")

def print_kwargs(**kwargs):
    print(" ", kwargs)
    
print_kwargs(
    kwargs_1 = "Shark",
    kwargs_2 = 4.5,
    kwargs_3 = True
)

input("\n Press Enter to Continue...")
print_header("Names")

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("  The value of {} is {}".format(key, value))
        
print_values(
    my_name = "Sammy",
    your_name = "Casey"
)

print() # Spacer

print_values(
    name_1 = "Alex",
    name_2 = "Gray",
    name_3 = "Harper",
    name_4 = "Phoenix",
    name_5 = "Remy",
    name_6 = "Val"
)

input("\n Press Enter to Continue...")
print_header("Ordering Arguments")

# Order of parameters
def example(arg_1, arg_2, *args, **kwargs):
    pass

def example2(arg_1, arg_2, *args, kw_1 = 1, kw_2 = "blobfish", **kwargs):
    pass

input("\n Press Enter to Continue...")
print_header("Some Args")

def some_args(arg_1, arg_2, arg_3):
    print("  arg_1:", arg_1)
    print("  arg_2:", arg_2)
    print("  arg_3:", arg_3)
    
args = ("sammy", "Casey", "Alex")
some_args(*args)

print() # Spacer

my_list = [2,3]
some_args(1, *my_list)

input("\n Press Enter to Continue...")
print_header("Keyworded")

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("  kwarg_1:", kwarg_1)
    print("  kwarg_2:", kwarg_2)
    print("  kwarg_3:", kwarg_3)
    
kwargs = {
    "kwarg_1" : "Val",
    "kwarg_2" : "Harper",
    "kwarg_3" : "Remy"
}
    
some_kwargs(**kwargs)

input("\n Press Enter to Continue...")
print_header("Ordering Arguments")
