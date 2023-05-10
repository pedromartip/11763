import os
from typing import Sequence


def filepath(filename, subfolder='data'):
    folder = os.path.dirname(__file__)
    return f'{folder}/{subfolder}/{filename}'


def str_floats(sequence_of_floats: Sequence[float]) -> str:
    if not sequence_of_floats:
        return '(None)'
    return f'({", ".join([f"{coord:0.02f}" for coord in sequence_of_floats])})'


def str_quaternion(q: tuple[float, float, float, float]) -> str:
    if not q:
        return '[None]'
    return f'{q[0]} + {q[1]}i + {q[2]}j + {q[3]}k'
