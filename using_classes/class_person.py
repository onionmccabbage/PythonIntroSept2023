# we will capture some aspects of a 'Person'
# we will store 'name' (a non empty string)
# 'age' (an integer)
# 'language' (a non-empty string)

class Person:
    '''This class enclapsulates a person
    we store name, age and language'''
    def __init__(self, n, a, l): # every function in a class MUST take 'self' as an argument
        print('a Person instance is being created')
        self.n = n
        self.a = a
        self.l = l
    def setName(self, new_name):
        if len(new_name)>0 and type(new_name)==str:
            self.n = new_name
        else:
            self.n = 'default'

if __name__ == '__main__':
    # we can create instances of our class
    Arianne = Person('Arianne', 42, 'Python') # every time we make an instance it will run __init__
    Betty   = Person('Betty', 35, 'Java')
    Con     = Person('Con', 23, 'Python')
    Arianne.setName('')
        
    # we can access any properties like this (called 'dot notation')
    print( Arianne.n, Arianne.a, Arianne.l )


   


