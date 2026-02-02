from utils import get_filepath, utf8len
import os
from hash_index_store import get_index_store, update_index_store


def put_handler(key: str, value: str):
    filepath = get_filepath("append_log.txt")

    with open(filepath, "a") as file:
        file_offset = os.path.getsize(filepath)
        string_offset = "PUT|" + key + "|"
        append_string = "PUT|" + key + "|" + value + "\n"
        string_byte_length = utf8len(string_offset)
        update_index_store(key, file_offset + string_byte_length)
        file.write(append_string)
    return
