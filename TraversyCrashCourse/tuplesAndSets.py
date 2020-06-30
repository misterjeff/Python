# A tuple is a collection which is ordered and unchangeable. Tuples allow duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
fruits3 = ('Apples',)  # If only initializing with one element, remember to include a trailing comma

# print(fruits, fruits2)
# print(fruits3, type(fruits3))

# Get value
print(fruits[1])

# Can't change values
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length of tuple
print(len(fruits))


# A set is a collection which is unordered and unindexed. Sets do not allow duplicate members.

# Create set
vegetables = {'Carrots', 'Potatoes', 'Celery'}

# Check if in set
print('Potatoes' in vegetables)

# Add to set
vegetables.add('Corn')

# Add duplicate
vegetables.add('Carrots')  # No error, the set just only keeps one value of Carrots

# Remove from set
vegetables.remove('Celery')

# Clear set contents
# vegetables.clear()

# Delete set
# del vegetables

print(vegetables, type(vegetables))