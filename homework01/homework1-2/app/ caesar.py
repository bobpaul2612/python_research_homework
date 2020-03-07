import sys


def _caecerEncrypt(words, shift):
    '''
    The function _caecerEncrypt execute caesar cipher encryption
    '''
    ciper = ''

    for i in words:
        ciper += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))

    print('\nThe encrypt result is : ' + ciper + '\n')

    return ciper


def _caecerDecrypt(words, shift):
    '''
    The function _caecerDecrypt execute cassar cipher decrytion
    '''
    plaintext = ''

    for i in words:
        plaintext += chr((ord(i) - ord('a') - shift) % 26 + ord('a'))

    print('\nThe decrypt result is : ' + plaintext + '\n')

    return plaintext


def caecerCipher(operation, words, shift):
    if operation == 'e':
        return _caecerEncrypt(words, shift)
    elif operation == 'd':
        return _caecerDecrypt(words, shift)


def _getInput():
    '''
    The _getInput function will get user input
    operation : the encryption / decryption operation
    words : you want to e/d's words
    shift : shift alpha
    '''
    try:
        operation, words, shift = input(
            'The input description\nopration , words , shift (below is example)\n    e \t   apple    5 \n    d \t   ecde     5 \nplease enter the opration : ').split()

        operation = operation.lower()

        if (operation != 'e') & (operation != 'd'):
            print('operation input error ! (only can input e/d)')
            raise ValueError

        if (not words.isalpha()) | (words != words.lower()):
            print('words input error ! (only can input alpha)')
            raise ValueError

        if (not shift.isdigit()) | (int(shift) < 0) | (int(shift) > 25):
            print('shift input error ! (only can input number)')
            raise ValueError

        shift = int(shift)

        return operation, words, shift

    except ValueError:
        print('The input is illegal !')
        print('Please input currect format (e apple 5)')
        raise ValueError


def main():
    '''
    aaa
    '''
    while True:
        try:
            operation, words, shift = _getInput()
        except:
            sys.exit(-1)

        caecerCipher(operation, words, shift)


if __name__ == "__main__":
    main()
