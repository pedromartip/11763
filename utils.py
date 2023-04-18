import os


def filepath(filename, subfolder='data'):
    folder = os.path.dirname(__file__)
    return f'{folder}/{subfolder}/{filename}'
