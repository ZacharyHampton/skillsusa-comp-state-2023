def _replace_step(number: str) -> str:
    """
    Completes first step of encryption, or last step of decryption

    :param number: four-digit number
    :return: str: number
    """

    #: Replace each digit by the (sum of itself + 7) mod 10
    return "".join(
        [str((int(string_number) + 7) % 10) for string_number in number]
    )


def _swap(number: str, index_one: int, index_two: int) -> str:
    """

    :param number: number
    :param index_one: 1st index to swap
    :param index_two: 2nd index to swap
    :return: str: number
    """

    numbers = list(number)

    first = numbers[index_one]
    numbers[index_one] = numbers[index_two]
    numbers[index_two] = first

    number = ''.join(numbers)

    return number


def encrypt(number: str) -> str:
    """
    Encrypts number using the following algorithm:
    - Replace each digit by (the sum of that digit plus 7) modulus 10.
    - Then swap the first digit with the third.
    - Then swap the second digit with the fourth.

    :param number: four-digit number
    :return: int: encrypted number
    """

    #: Replace each digit by the (sum of itself + 7) mod 10
    number = _replace_step(number)

    #: Swap first digit with the third
    number = _swap(number, index_one=0, index_two=2)

    #: Swap second digit with the fourth
    number = _swap(number, index_one=1, index_two=3)

    return number
