from utils import get_filepath, utf8len
import os
from pathlib import Path
import json


INDEX_FILE = Path.home() / ".my_index.json"


class IndexStore:
    def __init__(self):
        self.data = self.__load_from_disk()

    def __load_from_disk(self):
        if INDEX_FILE.exists():
            with open(INDEX_FILE) as f:
                return json.load(f)
        return {}

    def _save_to_disk(self):
        """Persist index map to disk"""
        with open(INDEX_FILE, "w") as f:
            json.dump(self.data, f)

    def get_index_store(self):
        """returns global index_store"""
        return self.data

    def update_index_store(self, key: str, bytes_offset: bytes) -> None:
        """Updates index store with byte offset"""
        try:
            self.data[key] = bytes_offset
            self._save_to_disk()
        except Exception as e:
            print("error", e)

    def load_index_store(self):
        """loads index_store if empty"""
        filepath = get_filepath(filename="append_log.txt")
        bytes_offset = 0
        self.data = {}

        with open(filepath) as f:
            for line in f:
                line_list = line.split("|")
                key = line_list[1]

                string_offset = utf8len(line_list[0] + "|" + line_list[1] + "|")

                self.update_index_store(key, string_offset + bytes_offset)
                bytes_offset += utf8len(line)
        self._save_to_disk()
