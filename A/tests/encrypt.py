from encryption.encryption import encrypt
import pytest


@pytest.mark.parametrize("number,encrypted_number", [("1234", "0189"), ["9562", "3962"]])
def test_encryption(number: int, encrypted_number: int):
    assert encrypt(number) == encrypted_number
