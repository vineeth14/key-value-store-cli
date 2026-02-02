import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_filepath(filename: str) -> str:
    """helper func that returns filepath given a filename"""
    filepath = os.path.join(BASE_DIR, filename)
    return filepath


def utf8len(s) -> int:
    """Returns byte length of string"""
    return len(s.encode("utf-8"))
