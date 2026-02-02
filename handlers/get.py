from utils import get_filepath


def get_handler(key: str):
    filepath = get_filepath("append_log.txt")

    with open(filepath) as file:
        for line in file.readlines()[::-1]:
            line = line.split("|")
            if line[1] == key:
                return line[2]
    return "key does not exist"
