import random
import string


def random_lower_string() -> str:
    """ random string for test"""
    return "".join(random.choices(string.ascii_lowercase, k=32))
