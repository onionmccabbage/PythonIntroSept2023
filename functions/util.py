def prettyPrint(n):
    output = ''
    for k,v in n.items():
        output += f'{k} contains {v}\n'
    return output

print(f'This module is called {__name__}')

if __name__ == '__main__':
    n = {'a':1, 'b':True}
    print( prettyPrint(n) )