# String in python are surrounded by either single or double quotes.

name = 'Higgins'
age = 42

# Concatenation
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String formatting

# Arguments by position
# print('My name is {name} and I am {age}.'.format(name = name, age = age))  # Notice no casting of age

# F-strings (Python 3.6+)
# print(f'Hello, my name is {name} and I am {age}.')

# String methods
s = 'hello world'

# Capitalize string
print(s.capitalize())  # Note the parentheses because 'capitalize' is a method

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case
print(s.swapcase())

# Get string length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))  # Returns True or False

# Ends with
print(s.endswith('d'))  # Returns True or False

# Split
print(s.split())  # Splits string into a list on space character

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())  # False because of space

# Is all alphabetic
print(s.isalpha())  # False because of space

# Is all numeric
print(s.isnumeric())  # False because of space