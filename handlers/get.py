from utils import get_filepath
from hash_index_store import IndexStore


def get_handler(index_store: IndexStore, key: str):
    filepath = get_filepath("append_log.txt")
    _index_store = index_store.get_index_store()

    if key in _index_store:
        offset = _index_store[key]
    else:
        return "key  not found"

    with open(filepath, "r") as file:
        file.seek(offset)
        return file.readline()
