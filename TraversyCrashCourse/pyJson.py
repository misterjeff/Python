# JSON is commonly used with data APIs.
# We can parse JSON into a Python dictionary.

import json

# Sample JSON
userJson = '{"firstName": "Louis", "lastName": "Higgins", "age": 42}'

# Parse to dictionary
user = json.loads(userJson)

print(user)
print(user['firstName'])

# Parse dictionary to JSON
car = {'Make': 'Ford', 'Model': 'Mustang', 'Year': 1970}
carJson = json.dumps(car)

print(carJson)