import random
import string

def generate_random_password(length: int, num_numbers: int, num_uppercase: int, num_special: int):
    password = ""
    for i in range(num_numbers):
        password += random.choice(string.digits)
    for i in range(num_uppercase):
        password += random.choice(string.ascii_uppercase)
    for i in range(num_special):
        password += random.choice(string.punctuation)
    for i in range(length - (num_numbers + num_uppercase + num_special)):
        password += random.choice(string.ascii_lowercase)
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    return password