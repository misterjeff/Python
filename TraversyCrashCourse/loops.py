# A for loop is used for iterating over a sequence (either a list, tuple, set, dictionary, or string)

people = ['John', 'Paul', 'Sarah', 'Susan']

# For loop
for person in people:
    print(f'Current person: {person}')

# Break
for person in people:
    if person == 'Sarah':
        break  # Loop execution stops if the condition is met
    print(f'Current person (break): {person}')

# Continue
for person in people:
    if person == 'Sarah':
        continue  # Loop execution skips to next iteration if condition is met
    print(f'Current person (continue): {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')



# While loops execute a set of statements as long as a condition is true

count = 0

# While
while count <= 10:
    print(f'Count: {count}')
    count += 1