import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_filepath(filename: str) -> str:
    filepath = os.path.join(BASE_DIR, filename)
    return filepath
