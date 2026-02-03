import argparse
from handlers.put import put_handler
from handlers.get import get_handler
from handlers.delete import del_handler
import traceback

from hash_index_store import IndexStore


def main():
    try:
        index_store = IndexStore()

        if not index_store.get_index_store():
            index_store.load_index_store()

        parser = argparse.ArgumentParser()

        subparser = parser.add_subparsers(dest="subcommand")

        put_subparser = subparser.add_parser(name="put", help="put command")
        put_subparser.add_argument("key")
        put_subparser.add_argument("value")

        get_subparser = subparser.add_parser(name="get", help="get command")
        get_subparser.add_argument("key")

        del_subparser = subparser.add_parser(name="del", help="del command")
        del_subparser.add_argument("key")

        args = parser.parse_args()

        commands = {
            "put": lambda: put_handler(
                index_store=index_store, key=args.key, value=args.value
            ),
            "get": lambda: get_handler(index_store=index_store, key=args.key),
            "del": lambda: del_handler(index_store=index_store, key=args.key),
        }

        command_func = commands.get(args.subcommand)

        if command_func:
            print(command_func())
        else:
            parser.print_help()
    except Exception:
        print(traceback.format_exc())


if __name__ == "__main__":
    main()
