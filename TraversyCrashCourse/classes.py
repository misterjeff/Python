# A class is like a blueprint for creating objects.
# An object has properties and methods (class functions) associated with it)
# Almost everything in Python is an object.

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def Greeting(self):
        return f'My name is {self.name}, and I am {self.age} years old.'
    
    def HasBirthday(self):
        self.age += 1

# Initialize User object
higgins = User('Louis Higgins', 'lhiggins@gmail.com', 42)

print(type(higgins))
print(higgins.name)

higgins.HasBirthday()
print(higgins.Greeting())

# Extend class (class inheritance)
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def SetBalance(self, balance):
        self.balance = balance
    
    # Method override
    def Greeting(self):
        return f'My name is {self.name}, and I am {self.age} years old. My balance is {self.balance}.'

jameson = Customer('James Jameson', 'jjameson@jjs.com', 69)
jameson.SetBalance(375)
print(jameson.Greeting())