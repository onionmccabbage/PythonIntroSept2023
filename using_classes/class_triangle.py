from class_shapes import Shape

class Triangle(Shape):
    def __init__(self, num_sides, x, y):
        super().__init__(num_sides) # this calls the __init__ of the parent class
        self.x = x
        self.y = y
    @property
    def x(self): # this is the getter method
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==float or type(new_x)==int:
            self.__x = new_x
        else:
            self.__x = 3 # set x to a safe default value
    @property
    def y(self): # this is the getter method
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y)==float or type(new_y)==int:
            self.__y = new_y
        else:
            self.__y = 4 # set x to a safe default value    

if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    t1.x = 'oh dear' # here we directly access the x property of the Tyiange instace
    t1.y = 3.6
    print(f'{t1.num_sides} sides {t1.x} by {t1.y}')