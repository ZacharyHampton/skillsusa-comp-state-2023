from argparse import ArgumentParser, Namespace
import argparse
import encryption


def main(args: list[str] | None = None) -> None:
    parser = ArgumentParser(
        prog="encryption",
        description="A program to encrypt four-digit integers.",
    )

    parser.add_argument(
        "number",
        type=str,
    )

    parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType('r')
    )

    parser.add_argument(
        "-o",
        "--output-file",
        type=argparse.FileType('w')
    )

    args: Namespace = parser.parse_args(args)

    print(encryption.encrypt(args.number))

