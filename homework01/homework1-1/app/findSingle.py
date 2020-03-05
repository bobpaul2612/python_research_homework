'''
This is the find single number from string
'''

import sys

def _getInput():
    '''
    The getInput function will get the user input
    '''
    inputString = input('Please enter English(only) string : ')

    try:
        if inputString.isalpha():
            return inputString
        else:
            raise ValueError
    except ValueError:
        print('The input include illegal charector')
        raise ValueError
        
            


def _findSingle():
    '''
    The findSingle function will find the single charector
    by the User input
    '''
    inputString = _getInput()
    print(inputString)


def main():
    '''
    The main function will execute the findSingle() 
    to find the single charector (only one)
    '''
    _findSingle()

if __name__ == "__main__":
    main()