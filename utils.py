import os


def filepath(filename, subfolder='data'):
    folder = os.path.dirname(__file__)
    return f'{folder}/{subfolder}/{filename}'

def str_quaternion(q: tuple[float, float, float, float]) -> str:
    return f'{q[0]} + {q[1]}i + {q[2]}j + {q[3]}k'
