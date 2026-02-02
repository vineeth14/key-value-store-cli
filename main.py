import argparse
from handlers.put import put_handler
from handlers.get import get_handler
from handlers.delete import del_handler


def main():
    try:
        parser = argparse.ArgumentParser()

        subparser = parser.add_subparsers(dest="subcommand")

        put_subparser = subparser.add_parser(name="put", help="put command")
        put_subparser.add_argument("key")
        put_subparser.add_argument("value")

        get_subparser = subparser.add_parser(name="get", help="get command")
        get_subparser.add_argument("key")

        args = parser.parse_args()

        commands = {
            "put": lambda: put_handler(key=args.key, value=args.value),
            "get": lambda: get_handler(key=args.key),
        }

        command_func = commands.get(args.subcommand)

        if command_func:
            print(command_func())
        else:
            parser.print_help()
    except Exception as e:
        print("error", e)


if __name__ == "__main__":
    main()
