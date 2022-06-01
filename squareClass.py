from rectangleClass import Rectangle

class Square(Rectangle):
    def __init__(self, length:str = 1.0, width:str = 1.0):
        super().__init__()
        self._length = length
        self._width = width
    
    
    def getSide(self):
        return self._length

    def setSide(self, length:str):
        self._length = length


    def setWidth(self, width:str):
        self._witdh = width

 
    def setLength(self, length:str):
        self._length = length

   
    def __str__(self):
        return (f"Square[Rectangle[Shape[color= {self._color},filled= {self._filled}],length= {self._length},width= {self._width}]]")
        

square1 =  Square(8, 8)    
print("Perimeter of square1 is:", square1.getPerimeter())
print("Area of square1 is:", square1.getArea())
print("Color of square1:", square1.getColor())
print("Is square1 filled ? ", square1.getFilled())
square1.setColor("Blue")
print("Color of square1:", square1.getColor())

print(square1)