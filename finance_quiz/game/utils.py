from random import randint
from game.models import User


def fingerprint_generator():
    fingerprint = ''
    for i in range(0, 100):
        fingerprint += f'{chr(randint(33, 124))}'

    try:
        User.objects.filter(session_fingerprint=fingerprint)
        fingerprint_generator()
    except:
        return fingerprint

