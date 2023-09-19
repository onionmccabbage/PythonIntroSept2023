# we already know a bit about functions...

def fnA(a, b): # these are called positional arguments
    return a+b

def fnB(m, n):
    return m**n

# we can choose to capture the arguments like this
# *args will gather ANY positional arguments into a tuple called 'args'
def fnC(*args):
    ''' combine name, age and lang into a string'''
    return f'Name: {args[0]} is {args[1]} years old and knows {args[2]}'

# **kwargs will gather ANY keyword arguments into a dictionary called 'kwargs'
def fnD(**kwargs):
    ''' show all the keyword arguments'''
    return kwargs # this will return a dict

if __name__ == '__main__':
    # the position of the arguments matters
    answer = fnA(77, 124)
    answer = fnA(a=9, b=3) # we can pass either positional or keyword arguments
    print(answer)
    # keyword arguments can be in any order
    p = fnB(n=3, m=5) # 125
    # NB positional args MUST come before any keyword args
    p = fnB(4, n=2) # we can even choose to pass some positional and some keyword args
    print(p)
    print( fnC('Bert', 42, 'ES') )
    print( fnD(type='admin', username='Neueda', pwd='c0nygre') )