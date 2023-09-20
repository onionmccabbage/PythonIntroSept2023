from class_shapes import Shape

class Triangle(Shape):
    # we can declare propertties that belong to the class itself
    count = 0 # this is like a 'static' property of the class
    def __init__(self, num_sides, x, y):
        super().__init__(num_sides) # this calls the __init__ of the parent class
        self.x = x
        self.y = y
        # increment the 'count'
        Triangle.count += 1
    @property
    def x(self): # this is the getter method
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x)==float or type(new_x)==int:
            self.__x = new_x
        else:
            self.__x = 3 # set x to a safe default value
    @property # @property is entirely optional. It has been available since Py 3.5
    def y(self): # this is the getter method
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y)==float or type(new_y)==int:
            self.__y = new_y
        else:
            self.__y = 4 # set x to a safe default value  
    # we can derive the hypotenuse of a right-angle triangle  
    @property # we ONLY declare a getter (no setter)
    def hypot(self): # this is now a read-only property
        h = (self.x**2 + self.y**2)**0.5
        return h
    # there is always a built-in __str__ method. we can choose to overide it with our own method
    # every time we call 'print' (on this class) it will use our __str__ method
    def __str__(self):
        return f'''This triangle has {self.num_sides} sides.
It measures {self.x} by {self.y}.
The Hypotenuse is {self.hypot:0.2f}'''

# by the way, whenever you find something in Python that has __...__
# that is a built-in part of Python

if __name__ == '__main__':
    t1 = Triangle(3, 4, 5)
    t2 = Triangle(3, -4,-5)
    t3 = Triangle(3, 7, 2)
    print(f'There are {Triangle.count} triangles')
    t1.x = 'oh dear' # here we try to directly access the x property of the Triange instace
    t1.y = 4 # this uses the y setter method to set __y
    print(f'{t1.num_sides} sides {t1.x} by {t1.y} has h={t1.hypot}')
    # we can choose to access the 'count' from any instance of the Triangle class
    t4 = Triangle(3, 435743, 53673463)
    print(f'we have {t4.count} triangles')
    print(t4)
