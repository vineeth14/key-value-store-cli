from utils import get_filepath, utf8len

_index_store = {}


def get_index_store():
    """returns global index_store"""
    return _index_store


def load_index_store():
    """loads index_store if empty"""
    filepath = get_filepath(filename="append_log.txt")
    bytes_offset = 0
    with open(filepath) as f:
        for line in f:
            line_list = line.split("|")
            key = line_list[1]

            string_offset = utf8len(line_list[0] + "|" + line_list[1] + "|")

            update_index_store(key, string_offset + bytes_offset)
            bytes_offset += utf8len(line)


def update_index_store(key: str, bytes: bytes) -> None:
    """Updates index store with byte offset"""
    try:
        _index_store = get_index_store()
        _index_store[key] = bytes
        return
    except Exception as e:
        print("error", e)
