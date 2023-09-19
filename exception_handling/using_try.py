# Sometimes there is a risk things might go wrong
# Python will raise an exception
# We can choose what to do with exceptions

def askUser():
    '''ask the user to enter a number'''
    # remember every 'input' is ALWAYS a string
    age = input('Please enter a number: ')
    # we need to store this as a numeric value
    # this will fail if the value is not numeric
    try:
        age_int = int(age)
        print(age_int)
    except ValueError as e: # handle specific kind of error
        print (f'Value Error: {e}')
    except Exception as e: # handle any other kind of error
        print(f'Generic Exception: {e}')
    finally: # optional
        print('The finally block will always run, whether or not there is an error')

if __name__ == '__main__':
    askUser() # invoke our function (run it)