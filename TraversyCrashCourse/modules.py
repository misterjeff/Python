# A module is a file containing a set of functions that you may include in your application.
# There are core Python modules, modules you can install using the Python Package Manager (PIP) - including Django -
#   as well as custom modules.

import datetime
from datetime import date  # Just import date from datetime module
import time
from time import time  # Just import time from time module

# Import custom module
import emailValidator
from emailValidator import ValidateEmail

today = datetime.date.today()
todayJustDate = date.today()

print(today, todayJustDate)

# timestamp = time.time()
timestamp = time()

print(timestamp)

email = 'test@test.com'

if(ValidateEmail(email)):
    print('Email is valid')
else:
    print('Email is invalid')