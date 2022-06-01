from shapeClass import Shape 
import math

class Circle(Shape):
    def __init__(self, radius: str = 1.0):
        super().__init__()
        self._radius = radius

    def getRadius(self):
        return self._radius

    def setRadius(self, radius: str):
        self._radius = radius

  
    def getArea(self):
        return math.pi * self._radius ** 2


    def getPerimeter(self):
        return 2 * math.pi * self._radius

    def __str__(self):
        return (f"Circle[Shape[Color= {self._color},Filled= {self._filled}],Radius= {self._radius}]")

circle1 =  Circle(16)
print("Perimeter of circle1 is:", circle1.getPerimeter())
print("Area of circle1 is:", circle1.getArea())
print("Color of circle1:", circle1.getColor())
print("Is circle1 filled? ", circle1.getFilled())
circle1.setColor("Yellow")
print("Color of circle1:", circle1.getColor())

print(circle1)