'''
This is the find single number from string
'''

import sys

len_limit = 100


def _get_input():
    '''
    The getInput function will get the user input
    '''
    alpha_str = input('Please enter English(only) string : ')

    try:
        if alpha_str.isalpha() & (len(alpha_str) < len_limit):
            return alpha_str
        else:
            raise ValueError
    except ValueError:
        print('The input include illegal charector')
        raise ValueError


def find_single_letter(alpha_str):
    '''
    The findSingle function will find the single charector
    by the User input

    return the single charector
    '''
    if (not alpha_str.isalpha()) or len(alpha_str) >= 100:
        return 'The input format error!'

    letter_list = [letter for letter in set(
        alpha_str) if alpha_str.count(letter) % 2]

    if len(letter_list) > 1:
        return "More than one single letter!"
    elif len(letter_list) == 0:
        return "No single letter in input string!"

    return letter_list[0]


def main():
    '''
    The main function will execute the findSingle()
    to find the single charector (only one)
    '''
    while True:
        try:
            alpha_str = _get_input()
        except:
            sys.exit(-1)

        single_letter = find_single_letter(alpha_str)

        if len(single_letter) == 1:
            print('The single charector is : ', single_letter)
        else:
            print(single_letter)


if __name__ == "__main__":
    main()
