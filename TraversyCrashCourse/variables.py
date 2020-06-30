# A variable is a container for a value, which can be of various types.

'''
This is a multi-line comment
a.k.a. docstring (used to define a function's purpose).
Either single quotes (as done here) or double quotes may be used.
'''

"""
Variable Rules:
  - Variable names are case sensitive
  - Variable names must start with a letter or underscore
  - Variable names can contain numbers but cannot start with a number
"""

# x = 1  # int
# y = 2.5  # float
# name = 'Higgins'  # string
# is_diggin = True  # bool

# Multiple assignment
x, y, name, is_diggin = (1, 2.5, 'Higgins', True)

# Basic math
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

# print(x, y, name, is_diggin, a)
print(type(y), y)
print(type(z), z)