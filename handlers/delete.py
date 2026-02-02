from hash_index_store import IndexStore
from utils import get_filepath


def del_handler(index_store: IndexStore, key: str):
    _index_store = index_store.get_index_store()

    if key in _index_store:
        del (_index_store, key)
        add_tombstone(index_store, key)
    else:
        return "key does not exist"


def add_tombstone(index_store: IndexStore, key: str):
    filepath = get_filepath("append_log.txt")

    with open(filepath, "a") as file:
        tombstone = "DEL|" + key
        file.write(tombstone)
    return
