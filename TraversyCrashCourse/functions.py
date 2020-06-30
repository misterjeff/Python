# A function is a block of code which only runs when it is called.
# In Python, indentation with tabs or spaces is used instead of braces.

# Create function
def sayHello(name):
    print(f'Hello, {name}.')

# Default parameters
def sayHelloDefault(name='you'):
    print(f'Hello, {name}.')

# Call function
sayHello('Higgins')
sayHelloDefault()

# Return values
def getSum(val1, val2):
    total = val1 + val2  # The total variable is only within the scope of the getSum function
    return total

result = getSum(12, 4)
print(getSum(3, 4), result)



# A lambda function is a small, anonymous function.
# A lambda function can take any number of arguments but can only have one expression (similar to arrow function in JS).

# Create lambda function
getSumMore = lambda val1, val2 : val1 + val2

print(getSumMore(10, 3))