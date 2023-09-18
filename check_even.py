# mini-challenge: ask the user for a number, then check if it is an even number

def askUser():
    ''' ask the user for a number '''
    n = input('Please enter a number: ')
    n_i = int(n)
    return n_i

def checkEven(e):
    '''check if a number is even'''
    if e%2 == 0: # an even number is divisible by 2
        return f'{e} is an even number'
    else:
        return f'{e} is not an even number'
    
# use our functions
s = askUser()
t = checkEven(s)
print(t)