from turtle import shape
from shapeClass import Shape
import math

class Equilateral_Triangle(Shape):
    def __init__(self, sidelength:str= 1.0):
        super().__init__()
        self._length = sidelength
 
    
    def getSideLength(self):
        return self._length

    def setSideLength(self, sidelength:str):
        self._length = sidelength

    def getArea(self):
        return (math.sqrt(3)/ 4)*(self._length * self._length)

    def getPerimeter(self):
        return 3 * (self._length)

    def __str__(self):
        return (f"Equilateral Triangle[Shape[color= {self._color},filled= {self._filled}],length= {self._length}]")

equilateralTriangle1 =  Equilateral_Triangle(8)  

print("Length of side is:", equilateralTriangle1.getSideLength())
print("Perimeter of equilateralTriangle1 is:", equilateralTriangle1.getPerimeter())
print("Area of equilateralTriangle1 is:", equilateralTriangle1.getArea())
print("Color of equilateralTriangle1:", equilateralTriangle1.getColor())
print("Is equilateralTriangle1 filled ? ", equilateralTriangle1.getFilled())
equilateralTriangle1.setColor("Blue")
print("Color of equilateralTriangle1:", equilateralTriangle1.getColor())

print(equilateralTriangle1)