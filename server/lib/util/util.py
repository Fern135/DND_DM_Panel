import secrets
import string
import re
from validate_email_address import validate_email

class util:

    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
        + string.ascii_lowercase + string.hexdigits + string.octdigits
        
        self.email_regex = r'^\S+@\S+\.\S+$'

    def sort(list:list) -> list: # sort the incoming list
        return sorted(list)

    def generate_random_string(self, length):
        return ''.join(secrets.choice(self.characters) for _ in range(length))
    
    def is_valid_email(self, email):
        if re.match(self.email_regex, email):
            # Additional check for email existence (uses validate_email_address library)
            try:
                validate_email(email, verify=True)
                return True
            except ValueError:
                return False
        else:
            return False