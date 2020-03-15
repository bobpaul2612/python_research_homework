import pytest
import caesar


class testing_data:
    caesar_cipher_illegal_data = [
        ('de', 'apple', 5, -1),
        ('j', 'apple', 5, -1),
        ('A', 'apple', 5, -1),
        ('1', 'apple', 5, -1),
        ('%', 'apple', 5, -1),
        ('d', 'app%le', 5, -1),
        ('d', 'apple1', 5, -1),
        ('d', 'apple', 'A', -1),
        ('d', 'apple', '%', -1),
    ]
    caesar_cipher_encrypt_data = [
        ('e', 'apple', 5, 'fuuqj'),
        ('e', 'zxy', 5, 'ecd'),
        ('e', 'apple zxy', 5, 'fuuqj ecd'),
        ('e', 'zxy', 31, 'ecd')
    ]
    caesar_cipher_decrypt_data = [
        ('d', 'ecde', 5, 'zxyz'),
        ('d', 'fuuqj', 31, 'apple'),
        ('d', 'ecde fuuqj', 5, 'zxyz apple'),
    ]


@pytest.mark.parametrize("operation , words , shift , expected", testing_data.caesar_cipher_illegal_data)
def test_caesar_cipher_illegal_parameter(operation, words, shift, expected):
    # arrage

    # act
    result = caesar.caesar_cipher(operation, words, shift)

    # assert
    assert result == expected


@pytest.mark.parametrize('operation , words , shift , expected', testing_data.caesar_cipher_encrypt_data)
def test_caesar_cipher_encrypt_parameter(operation, words, shift, expected):
    # arrage

    # act
    result = caesar.caesar_cipher(operation, words, shift)

    # assert
    assert result == expected


@pytest.mark.parametrize('operation , words , shift , expected', testing_data.caesar_cipher_decrypt_data)
def test_caesar_cipher_decrypt_parameter(operation, words, shift, expected):
    # arrage

    # act
    result = caesar.caesar_cipher(operation, words, shift)

    # assert
    assert result == expected
