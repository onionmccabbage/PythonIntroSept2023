# Python has two scopes:
# everything is in the 'global' scope
# unless it is in a code block, then it is in a separate 'block' scope

# here is something in the global scope
g = 'this is in the global scope'

def fn():
    '''every function, class etc. has its own block scope'''
    global g # now we are accessing the same 'g' as declared globally
    g = 'this is in the scope of the function'

# as a general rule we tend to avoid putting stuff in the global scope
if __name__ == '__main__':
    fn()
    print(g)