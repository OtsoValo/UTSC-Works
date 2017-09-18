import math
case_angle = 90


class Parallelogram():
    ''' A class which has details about a Parallelogram.'''

    def __init__(self, base, side, theta):
        ''' (Parallelogram, float, float, float) -> NoneType
        The function will initialize base side and theta of a parallelogram.
        '''
        self._base = base
        self._side = side
        self._theta = theta

    def area(self):
        ''' (Parallelogram) -> float
        The function will calculate the area of the parallelogram:
        the area = base * side * sin(theta)
        '''
        return self._base * self._side * math.sin(math.radians(self._theta))

    def bst(self):
        ''' (Parallelogram) -> list of float
        The function will return a list of base, side and theta.
        '''
        result = [self._base, self._side, self._theta]
        return result

    def __str__(self):
        ''' (Parallelogram) -> str
        The function will return a str of shape and area.
        '''
        return 'I am a Parallelogram with area ' + str(self.area())


class Rectangle(Parallelogram):
    ''' A class which has details about a Rectangle, and a child class of
    Parallelogram'''

    def __init__(self, base, side):
        ''' (Rectangle, float, float) -> NoneType
        The functioninitialize detials of Rectangle by calling
        the method from parent class.
        '''
        Parallelogram.__init__(self, base, side, case_angle)

    def __str__(self):
        ''' (Rectangle) -> str
        The function will return a str of shape and area by calling the
        method from parent class.
        '''
        return 'I am a Rectangle with area ' + str(self.area())


class Rhombus(Parallelogram):
    ''' A class which has details about a Rhombus, and a child class of
    Parallelogram'''

    def __init__(self, base, theta):
        ''' (Rhombus, float, float) -> NoneType
        The functioninitialize detials of Rhombus by calling
        the method from parent class.
        '''
        Parallelogram.__init__(self, base, base, theta)

    def __str__(self):
        ''' (Rhombus) -> str
        The function will return a str of shape and area by calling the
        method from parent class.
        '''
        return 'I am a Rhombus with area ' + str(self.area())


class Square(Rectangle, Rhombus):
    ''' A class which has details about a Square, and a child class of
    Parallelogram'''

    def __init__(self, base):
        ''' (Square, float) -> NoneType
        The functioninitialize detials of square by calling
        the method from parent class.
        '''
        Rectangle.__init__(self, base, base)
        Rhombus.__init__(self, base, case_angle)

    def __str__(self):
        ''' (Square) -> str
        The function will return a str of shape and area by calling the
        method from parent class.
        '''
        return 'I am a Square with area ' + str(self.area())
