from encryption.encryption import encrypt, decrypt
import pytest


@pytest.mark.parametrize("number,encrypted_number", [("1234", "0189"), ["9562", "3962"]])
def test_encryption(number: str, encrypted_number: str):
    assert encrypt(number) == encrypted_number


@pytest.mark.parametrize("encrypted_number,number", [("0189", "1234"), ["3962", "9562"]])
def test_decryption(encrypted_number: str, number: str):
    assert decrypt(encrypted_number) == number
