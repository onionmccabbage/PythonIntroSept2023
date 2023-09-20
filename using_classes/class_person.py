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
    def getName(self):
        return self.__n
    def setName(self, new_name):
        if len(new_name)>0 and type(new_name)==str:
            self.__n = new_name
        else:
            self.__n = 'default'
    def getAge(self):
        return self.a
    def setAge(self, newAge):
        if type(newAge)==int:
            self.a = newAge
        else:
            pass # do nothing if the age is invalid
    def getLang(self):
        return self.l
    def setLang(self, new_lang):
        if type(new_lang)==str and len(new_lang)>0:
            self.l = new_lang
        else:
            pass
            # raise TypeError('Language must be a non emtpy string')
    n = property(getName, setName)

if __name__ == '__main__':
    # we can create instances of our class
    Arianne = Person('', 42, 'Python') # every time we make an instance it will run __init__
    Betty   = Person('Betty', 35, 'Java')
    Con     = Person('Con', 23, 'Python')
    # Arianne.setName('')
    Betty.setAge('old')
    Con.setLang(32)
        
    # we can access any properties like this (called 'dot notation')
    print( Arianne.n, Betty.a, Con.l )


   


