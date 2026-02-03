from hash_index_store import IndexStore
from utils import get_filepath


def del_handler(index_store: IndexStore, key: str) -> str | None:
    _index_store = index_store.get_index_store()
    if key in _index_store:
        add_tombstone(index_store, key)
        del _index_store[key]
        index_store._save_to_disk()
    else:
        return "key does not exist"


def add_tombstone(index_store: IndexStore, key: str) -> None:
    filepath = get_filepath("append_log.txt")

    with open(filepath, "a") as file:
        tombstone = "DEL|" + key + "\n"
        file.write(tombstone)
    return
