def checkValidInt(i):
    if type(i)==int or i.isdigit():
        return int(float(i))
    else:
        return 0
    
print(f'This module is called {__name__}')

if __name__ == '__main__':
    pass