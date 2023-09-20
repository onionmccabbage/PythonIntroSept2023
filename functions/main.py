from util import prettyPrint
from validate import checkValidInt
def main():
    l = []
    while len(l)<5: 
        n=input(f'Please enter value:')
        l.append( checkValidInt(n) )
    return l

print(f'This module is called {__name__}')

if __name__ == '__main__':
    l = main()
    d = {'A':l[0], 'B':l[1], 'C':l[2], 'D':l[3], 'E':l[4]}
    print( prettyPrint(d) )
