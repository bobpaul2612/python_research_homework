'''
implement caesar cipher system
'''
import sys

a_ascii = ord('a')
A_ascii = ord('A')
alpha_num = 26


def caesar_system(words, shift):
    def _caesar_operation(letter):
        if not letter.isalpha():
            return letter
        if letter.islower():
            this_ascii = a_ascii
        else:
            this_ascii = A_ascii

        letter_index = ord(letter) - this_ascii
        trans_letter_index = (letter_index + shift) % alpha_num
        new_letter = chr(trans_letter_index + this_ascii)
        return new_letter

    trans_words_map = map(_caesar_operation, words)

    return ''.join(list(trans_words_map))


def _caesar_input_check(operation, words, shift):
    if operation != 'e' and operation != 'd':
        return False
    elif not (words.replace(' ', '').isalpha()):
        return False
    elif not (isinstance(shift, int)):
        return False
    return True


def caesar_cipher(operation, words, shift):

    operation = operation.lower()

    if not _caesar_input_check(operation, words, shift):
        return -1

    if operation == 'e':
        return caesar_system(words, shift)
    elif operation == 'd':
        return caesar_system(words, -shift)


def _get_input():
    '''
    The _get_input function will get user input
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
            operation, words, shift = _get_input()
        except:
            sys.exit(-1)

        result = caesar_cipher(operation, words, shift)
        print(result)


if __name__ == "__main__":
    main()
