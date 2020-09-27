import random
import string


def generateCode(length):
    code = string.digits
    random_code = ''.join(random.choice(code) for i in range(length))
    return random_code

