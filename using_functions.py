# we can write code within functions  to make it re-useable

# here we write a function to calculate the square of a number
def makeSqr(n): # we can pass arguments in the brackets
    result = n*n
    return result

# we can give the arguments default values
def power(m=2,n=3):
    return m**n

def validAge():
    '''ask the user for a positive number''' # this is a docstring
    age = input('Please enter a positive number')
    # convert to an integer
    age_i = int(age)
    if age_i >=0:
        print(f'Age is {age_i}')
    else:
        print(f'Sorry, {age_i} is not valid')

# now we can use our function
print( makeSqr(2) ) # 4
print( makeSqr(3) ) # 9
print( makeSqr(5) ) # 25
r = power(4,3) # 64
print (r)
r = power() # uses the default values
print( r ) # 8
# run our age checker
validAge()