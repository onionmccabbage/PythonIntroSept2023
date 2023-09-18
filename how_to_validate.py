def isString(s):
    ''' return True if s is a string '''
    if type(s)==str:
        return True
    else:
        return False

def isInt(i):
    ''' return True if i is an integer '''
    if type(i)==int:
        return True
    else:
        return False

def isFloat(f):
    ''' return True if f is a floating point number '''
    if type(f)==float:
        return True
    else:
        return False

if __name__ == '__main__':
    # here is an int, a float and a str
    my_values = (3, 7.2, 'hello')
    # print( isString( my_values[2] ) , type(my_values[2]))
    for item in my_values:
        true_s = isString(item)
        true_i = isInt(item)
        true_f = isFloat(item)
        print( f'{item} string:{true_s} int:{true_i} float:{true_f}' )