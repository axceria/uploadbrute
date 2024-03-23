#!/usr/bin/env python3

import random
import string


# Generate a random string based on a given length

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length - 2))  # Subtract 2 for start and end letters
    random_string = random.choice(string.ascii_letters) + random_string + random.choice(string.ascii_letters)  # Ensure start and end with a letter
    random_string_list = list(random_string)
    for _ in range(5):  # Shuffle 5 times
        random.shuffle(random_string_list)
    random_string = ''.join(random_string_list)
    return random_string
