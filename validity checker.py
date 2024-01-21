import re 
import dns.resolver

def is_valid_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]')

    if not email_pattern.match(email):
        return False, "Invalid Email Format"

