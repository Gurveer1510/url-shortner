import string
import random

def generate_random_key():
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(6))
