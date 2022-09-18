class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def __str__(self):
        return f'Width {self._width} Height {self._height}'
    
    #FIX: create a static method returning a square instead of creating a Squre Class
    @staticmethod
    def square(size):
        return Rectangle(size, size)
    
    
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value 


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        self._width = self._height = value
    
    @height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    
    expected = int(w*10)
    print(f'Expected area {expected} \n Got {rc.area}')
    

if __name__ == '__main__':
    rc = Rectangle(2, 5)
    use_it(rc)
    sq = Square(5)
    use_it(sq)
    sq_fixed = Rectangle.square(5)
    use_it(sq_fixed)