# If/Else conditions are used to decide to do something based on something being True or False
x, y = (10, 20)


# Comparison operators (==, !=, >, <, >=, <=) are used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/Else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# Elif
if x > y:
    print(f'{x} is greater than {y}')
elif y > x:
    print(f'{y} is greater than {x}')
else:
    print(f'{x} is equal to {y}')

# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')



# Logical operators (and, or, not) are used to combine conditional statements

# And
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# Or
if x > 2 or x <= 10:
    print(f'{x} is either greater than 2 or less than or equal to 10')

# Not
if not(x == y):
    print(f'{x} is not equal to {y}')



# Membership operators (not, not in) are used to test if a sequence is present in an object

numbers = [1, 2, 3, 4, 5]

# In
if x in numbers:
    print(x in numbers)  # Returns True if true or nothing if false

# Not in
if x not in numbers:
    print(x not in numbers)  # Returns True if true or nothing if false



# Identity operators (is, is not) compare objects -
# not whether they are equal but whether they are actually identical (i.e. sharing the same memory location)

# Is
if x is y:
    print(x is y)  # Returns True if true or nothing if false

# Is not
if x is not y:
    print(x is not y)  # Returns True if true or nothing if false