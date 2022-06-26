from pathlib import Path
from src import create_testing_folder
import argparse
import os
import sys


def init_folders(args):
    folder = Path(os.getcwd())
    if args.config:
        config_file = Path(args.config[0]).resolve()
        config_file = Path(config_file)
        create_testing_folder.create_folders_with_config(folder, config_file)
    else:
        create_testing_folder.create_folders_with_default(folder, args.quant)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Initialize
    parser_init = subparsers.add_parser("init", help="Initialize the testing folders.")
    parser_init.add_argument(
        "quant",
        type=int,
        nargs="?",
        help="The test case you want to add in this folder.",
    )
    parser_init.add_argument(
        "--config", "-c", action="append", help="<Required> Set flag", required=False
    )

    parser_init.set_defaults(func=init_folders)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
