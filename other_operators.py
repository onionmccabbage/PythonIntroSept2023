# Python also supports += -= *= and /=
import random


def useOperators(a=9, b=1):
    ''' we can use short-cut operators'''
    a += b # we increment a by b
    b -= a # we decrement b by a
    a *= b # we multiply a by b and store in a
    b /= a # we divide b by a then store in b
    return (a, b) # here we return a tuple
    
if __name__ == '__main__':
    print( useOperators() ) # (-90, 0.1)
    print( useOperators(a=3, b=9) ) 