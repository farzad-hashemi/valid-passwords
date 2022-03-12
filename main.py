import string
from random import choices

def create_password(length = 8, upper=True, lower=True, digits=True, punc=True):
    pool = ""
    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digits:
        pool += string.digits

    if punc:
        pool += string.punctuation

    password = choices(pool, k=length)
    return ''.join(password)

print(create_password(15))