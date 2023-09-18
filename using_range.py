# ranges and __name__
def checkInRange(n):
    '''check to see if n is in a range of values'''
    # range(start, stop-before, step)
    r = range(0,100) # this range is the integers from 0 to 99
    if n in r:
        return f'{n} is in range'
    else:
        return f'{n} is not in the range'
    
# it is conventional to use __name__ in every python module
# by default Python ALWAYS sets __name__ to '__main__'
# (except for imports)
print( __name__ == '__main__') # True or False
# here is the convention
if __name__ == '__main__':
    a = checkInRange(105)
    print(a)