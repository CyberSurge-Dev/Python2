# Zachary Hoover || 9-13-23 || Guided Practice #11

from code import interact


def print_header(title):
    """Prints header with title."""
    print("\n ------+ " + title + " +------\n")
    return

print_header("Encapsulation")

class BankAccount:
    def __init__(self, account_number, balance):
        """Initialize the class"""
        self.account_number = account_number
        self.balance = balance

input("\n Press Enter to Continue...") 
print_header("Defining a Class")

account = BankAccount("123456789", 1000)
print(" ", account.balance)

input("\n Press Enter to Continue...")
print_header("Private Atrributes")

class BankAccount:
    def __init__(self, account_number, balance):
        """Initialize the class"""
        self.__account_number = account_number
        self.__balance = balance
     
input("\n Press Enter to Continue...")   
print_header("Protected Atrributes")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate
        
    def calculate_interest(self):
        return self.__balance * self.__interest_rate
    
input("\n Press Enter to Continue...")
print_header("Private Atrributes")
    
class BankAccount:
    def __init__(self, account_number, balance):
        """Initialize the class"""
        self.__account_number = account_number
        self.__balance = balance
        
    def __process_transaction(self, amount):
        if amount < 0:
            raise ValueError("Transaction amount must be positive.")
        self.__balance += amount
        
    def deposit(self, amount):
        self.__process_transaction(amount)
        
    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        
input("\n Press Enter to Continue...")
print_header("Name Mangling")

class MyClass:
    def __init__(self):
        self.__private_var = "This is a private variable."
    def __private_method(self):
        print("  This is a private method")
        
obj = MyClass()

# Accessing the private variable using name mangling
print(" ", obj._MyClass__private_var)
obj._MyClass__private_method()

input("\n Press Enter to Continue...")
print_header("Mangling Examples")

class Person:
    def __init__(self, name):
        self.__name = name
        
class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.__name = name # Create a naming conflict
        self.__employee_id = employee_id
        
employee = Employee("John", 12345)
print(" ", employee._Person__name) # Access using name mangling
print(" ", employee._Employee__name)

input("\n Press Enter to Continue...")
print_header("Implementing Private Methods")

account = BankAccount("123456789", 1000)
account._BankAccount__process_transaction(500) # Works, not recomended.

print(" ", account._BankAccount__balance)

input("\n Press Enter to Continue...")