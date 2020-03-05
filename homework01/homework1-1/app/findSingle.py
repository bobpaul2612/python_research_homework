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
        
            


def _findSingle(inputString):
    '''
    The findSingle function will find the single charector
    by the User input

    return the single charector
    '''
    mark = [0 for i in range(len(inputString))]
    ansIndex = -1

    for i in range(len(inputString)):
        if mark[i] == 1:
            continue
        for j in range(i+1 , len(inputString)):
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

def main():
    '''
    The main function will execute the findSingle() 
    to find the single charector (only one)
    '''
    while True:
        try:
            inputString = _getInput()
        except:
            sys.exit(-1)
    
        ans = _findSingle(inputString)

        if len(ans) == 1:
            print('The single charector is : ' , ans)
        else:
            print('This input no answer !')

if __name__ == "__main__":
    main()