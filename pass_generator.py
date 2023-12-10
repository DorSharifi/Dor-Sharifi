'''
The function generates a random 12 characters strong password, with upper and lower charecters, numbers and speciel symbols
'''
import random
import string

def generate_random_password():
    def generate_random_char():

        letters = string.ascii_letters
        numbers = string.digits
        special_chars = string.punctuation

        all_chars = letters + numbers + special_chars

        random_char = random.choice(all_chars)

        return random_char

    password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)

    password += ''.join([generate_random_char() for x in range(9)])

    return password

random_password = generate_random_password()
print("Random Password:", random_password)
