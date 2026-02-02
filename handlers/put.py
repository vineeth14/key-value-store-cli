from utils import get_filepath


def put_handler(key: str, value: str):
    filepath = get_filepath("append_log.txt")
    with open(filepath, "a") as file:
        file.write("PUT|" + key + "|" + value + "\n")
    return
