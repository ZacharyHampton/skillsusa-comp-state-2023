# Project A - Encryption

## CLI
```
usage: encryption [-h] [-a {encrypt,decrypt,clear,read}] [-f FILE] [-n NUMBER]

A program to encrypt four-digit integers.

options:
  -h, --help            show this help message and exit
  -a {encrypt,decrypt,clear,read}, --action {encrypt,decrypt,clear,read}
  -f FILE, --file FILE
  -n NUMBER, --number NUMBER
```

## Installation 
- Clone this repository.
- CD into the A directory (where we are now)
- Run `pip install .`
- Use the command `encryption` to run the software. 

## CLI Examples
- `encryption -n 1234 -a encrypt -f tests/logs.txt`
- `encryption -n 0189 -a decrypt -f tests/logs.txt`
- `encryption -a read -f tests/logs.txt`
- `encryption -a clear -f tests/logs.txt`

## Features
- Pytest Implementation (/tests)
- Proper Python CLI