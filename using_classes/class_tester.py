from class_person import Person

# any class can inherit from aother existing class
class Tester(Person):
    '''Tester inherits name, age and lang from Person
    We also add "permisson" as a property of Tester  '''
    def __init__(self, n, a, l, p):
        super().__init__(n, a, l) # we call the __init__ of Person
        self.p = p
    def getPermission(self):
        return self.__p
    def setPermission(self, new_permission):
        if type(new_permission)==str and len(new_permission)>0:
            self.__p = new_permission
        else:
            pass 
    p = property(getPermission, setPermission)

if __name__ == '__main__':
    t1 = Tester('Deidre', 30, 'C', 'admin')
    # we can change properties of our class instance
    t1.l = 'Python' # dot-notation will call the property getter or setter
    t1.p = 'super-user'
    print(f'{t1.n} knows {t1.l} and has {t1.p} access')
