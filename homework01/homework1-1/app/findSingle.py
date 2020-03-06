'''
This is the find single number from string
'''

import sys


def _getInput(lenLimit):
    '''
    The getInput function will get the user input
    '''
    inputString = input('Please enter English(only) string : ')

    try:
        if inputString.isalpha() & (len(inputString) < lenLimit ):
            return inputString
        else:
            raise ValueError
    except ValueError:
        print('The input include illegal charector')
        raise ValueError


def _findSingle(inputString):
    '''
    The findSingle function will find the single charector
    by the User input

    o(n^2) , and can't solve two single charector

    return the single charector
    '''
    mark = [0 for i in range(len(inputString))]
    ansIndex = -1

    for i in range(len(inputString)):
        if mark[i] == 1:
            continue
        for j in range(i+1, len(inputString)):
            if mark[j] == 1:
                continue
            if(inputString[i] == inputString[j]):
                mark[i] = mark[j] = 1

    for i in range(len(mark)):
        if mark[i] == 0:
            ansIndex = i

    if ansIndex != -1:
        return inputString[ansIndex]
    return 'This input no answer !'


def _findSingle_by52(inputString):
    '''
    The _findSing_by52 is the second approach to find the single charector
    o(n)
    '''
    alpha = [0 for i in range(52)]
    hashtable = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' ,'y' , 'z' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']
    ans = ''

    for i in inputString:
        if(ord(i) >= 97):
            # i is lower alpha
            alpha[ord(i)-ord('a')] ^= 1
        else:
            alpha[ord(i)-ord('A') + 26] ^= 1

    for i in range(len(alpha)):
        if (ans != '') & (alpha[i] != 0):
            return 'This input no answer !'
        elif alpha[i] != 0:
            ans = hashtable[i]

    return ans


def main():
    '''
    The main function will execute the findSingle()
    to find the single charector (only one)
    '''
    while True:
        try:
            inputString = _getInput(100)
        except:
            sys.exit(-1)

        ans = _findSingle_by52(inputString)

        if len(ans) == 1:
            print('The single charector is : ', ans)
        else:
            print('This input no answer !')


if __name__ == "__main__":
    main()
