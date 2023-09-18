# isnumeric and isdigit work like this...

a = '123'
b = '456.78'
c = 'one'

if a.isnumeric(): # isnumeric checks if a STRING looks like a number
    print(f'{a} is numeric')

if b.isnumeric():
    print(f'{b} is numeric')
else:
    print(f'{b} is not numeric')

if a.isdigit():
    print(f'{a} is digit')
else:
    print(f'{a} is not digit')

# Be careful isnumeric and isdigit will only check if there are numbers in a string - NOT - . etc.