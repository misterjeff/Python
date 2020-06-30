# A list is a collection which is ordered and changeable. Lists allow duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]  # More common way
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Using constructor
numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

# Get a single value from a list
print(fruits[1])  # Get element by index

# Get the length of a list
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Remove with pop
fruits.pop(2)

# Insert into position
fruits.insert(2, 'Strawberries')  # Insert Strawberries into the 3rd position

# Change value
fruits[0] = 'Blueberries'

# Reverse list contents
fruits.reverse()

# Sort list (alphabetically)
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)