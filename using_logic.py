# input, if, while, functions

# we can grab user input like this
n = input('please type your name: ') # this will wait for the user to enter stuff
print(n, type(n)) # caeful - EVERY input is a string-type
a = input('please type your age: ')
# we can try to convert a string to a number
a_float = float(a) # or int(a) to make it an integer
print( a, type(a), a_float, type(a_float) )
# we can format a string like this
print( f'welcome {n} your age is {a_float}' )
# alternative syntax does the same thing
print( 'welcome {} your age is {}'.format(n, a_float) )
# using 'if'
if a_float >0 and a_float <18: # < > <= >= or == (double-equals checks equality)
    print('you cant come in here')
elif a_float >= 18: # means else if
    print('you can come in')
else:
    print('age not recognized')

# 'while' will keep going until a value is met
# here we make sure the user enters a city
city = '' # here we have an empty string
while city !='': # != means not equal
    city = input('Please enter a city name: ')

print(f'You entered {city}')