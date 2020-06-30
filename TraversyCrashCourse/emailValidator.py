# Example of a custom module to be imported

# Import regular expressions library to assist in validation
import re

def ValidateEmail(emailAddress):
    if len(emailAddress) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", emailAddress))