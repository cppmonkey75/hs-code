class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'

class Square(Rectangle): # Square is a subclass of Rectangle
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self):
        return f'Square: side={self.side}'


s=Square(4)
print(s)