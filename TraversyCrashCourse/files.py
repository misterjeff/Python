# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get info from file
print(f'Name: {myFile.name}')
print(f'Is Closed: {myFile.closed}')
print(f'Opening Mode: {myFile.mode}')

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript.')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also like PHP...Just kidding.')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r')
text = myFile.read(100)
print(text)