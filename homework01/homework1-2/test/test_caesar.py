import pytest
import caesar


class testingData:
    encryptLigalTestData = [
        ('e', 'apple', 5, 'fuuqj'),
        ('e', 'xyz', 5, 'ecd'),
        ('d', 'ecde', 5, 'zxyz')
    ]


@pytest.mark.parametrize("operation , words , shift , expected", testingData.encryptLigalTestData)
def testEncryptLigalparameter(operation, words, shift, expected):
    # arrage

    # act
    result = caesar.caesarCipher(operation, words, shift)

    # assert
    assert result == expected
