# we will declare a generic 'shape' class then a specific 'triangle' class
# all 'shape' instances will have 'num_sides'
# the 'triangle' class will also have x and y and derive h

class Shape(object):
    def __init__(self, num_sides):
        self.num_sides = num_sides # this will call the @property setter
    @property # this is the 'getter'
    def num_sides(self):
        # 'mangling' is like 'private'
        return self.__num_sides # this 'mangles' the property to avoid direct access
    @num_sides.setter
    def num_sides(self, new_sides):
        if type(new_sides) == 'float' or type(new_sides)==int:
            self.__num_sides = new_sides
        else:
            pass

if __name__ == '__main__':
    square = Shape(4)
    hex    = Shape(6)
    hex.num_sides = 6.000 # Python makes the function appear like a property
    
    print(square.num_sides, hex.num_sides) # this will call the @property getter