from argparse import ArgumentParser, Namespace
import argparse
from encryption.encryption import encrypt, decrypt
import logging
import sys
import re


def main(args: list[str] | None = None) -> None:
    parser = ArgumentParser(
        prog="encryption",
        description="A program to encrypt four-digit integers.",
    )

    parser.add_argument(
        "-a",
        "--action",
        type=str,
        choices=["encrypt", "decrypt", "clear", "read"]
    )

    parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType('r+'),
        required=False
    )

    parser.add_argument(
        "-n",
        "--number",
        type=str,
        required=False
    )

    args: Namespace = parser.parse_args(args)
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    if args.number:
        if len(args.number) != 4 or not re.match(r"\d{4}", args.number):
            logger.fatal("Number is not a number, or is not 4 digits.")
            sys.exit(0)

    match args.action:
        case "encrypt":
            if args.number is None:
                logger.fatal("Number is required for this action (encrypt).")
                sys.exit(0)

            if args.file is None:
                logger.fatal("File is required for this action (encrypt).")
                sys.exit(0)

            result = encrypt(args.number)

            logs = args.file
            content = logs.read()
            logs.seek(0, 0)
            logs.write(result.rstrip('\r\n') + '\n' + content)

            logger.info(result)
        case "decrypt":
            if args.number is None:
                logger.fatal("Number is required for this action (decrypt).")
                sys.exit(0)

            result = decrypt(args.number)
            logger.info(result)
        case "clear":
            if args.file is None:
                logger.fatal("File is required for this action (clear).")
                sys.exit(0)

            with args.file as f:
                f.truncate(0)
        case "read":
            if args.file is None:
                logger.fatal("File is required for this action (read).")
                sys.exit(0)

            with args.file as f:
                lines = f.readlines()
                for number in lines:
                    number = number.rstrip()
                    result = decrypt(number)
                    logger.info(result)

