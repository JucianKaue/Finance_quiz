from random import randint
from game.models import User


def fingerprint_generator():
    hash = ''
    for i in range(0, 100):
        hash += f'{chr(randint(33, 124))}'

    try:
        User.objects.filter(session_hash=hash)
        fingerprint_generator()
    except:
        return hash
        f

