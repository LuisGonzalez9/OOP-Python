from curses.textpad import rectangle
from shapeClass import Shape

class Rectangle(Shape):
    def __init__(self, length:str=1.0, width:str=1.0):
        super().__init__()
        self._length = length
        self._width = width
    
    def rectangle():
        return ("Rectangle")
    

    def get_length(self):
        return self._length

    def set_length(self, length:str):
        self._length = length
    
    def getWidth(self):
        return self._width

    def setWidth(self, width:str):
        self._width = width

    def getArea(self):
        return self._length * self._width

    def getPerimeter(self):
        return 2 * (self._length + self._width)

  
    def __str__(self):
        return (f"Rectangle[Shape[color= {self._color},filled= {self._filled}],length= {self._length}, width= {self._width}]")

rectangle1 =  Rectangle(6, 7)    
print("Perimeter of this rectangle is:", rectangle1.getPerimeter())
print("Area of rectangle1 is:", rectangle1.getArea())
print("Color of rectangle1:", rectangle1.getColor())
print("Is rectangle1 filled ? ", rectangle1.getFilled())
print("Color of rectangle1:", rectangle1.getColor())

print(rectangle1)

