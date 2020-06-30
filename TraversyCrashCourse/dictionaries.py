# A dictionary is a collection which is unordered, changeable, and indexed. Dictionaries do not allow duplicate members.

# Create dictionary
person = {
    'firstName': 'Louis',
    'lastName': 'Higgins',
    'age': 42
}

# Using constructor
person2 = dict(firstName = 'Maybell', lastName = 'Haverford')

print(person, type(person))
print(person2, type(person2))

# Get value
print(person['firstName'])
print(person.get('lastName'))

# Add key/value
person['phone'] = '555-1234'

# Get dictionary keys
print(person.keys())

# Get dictionary items (key/value pairs)
print(person.items())

# Copy dictionary
person3 = person.copy()
person3['city'] = 'Springfield'

print(person3)

# Remove item
del person['age']
person.pop('phone')  # Another way to remove an item

# Clear a dictionary
person.clear()

# Get length
print(len(person3))

print(person)

# List of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)
print(people[1])