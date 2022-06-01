from abc import ABCMeta, abstractmethod
from turtle import circle, shape
from xml.etree.ElementTree import tostring

class Shape():
 
    __metaclass__ = ABCMeta

    def __init__(self, filled:bool= True, color:str="red"):
        self._filled = filled
        self._color = color 

    def getColor(self):
        return self._color

    def setColor(self, color:str):
        self._color = color
    
    def getFilled(self):
        return self._filled

    def setFilled(self, filled:bool):
        self._filled = filled

    @abstractmethod
    def getArea(self):
        pass
    @abstractmethod
    def getPerimeter(self):
        pass


    def __str__(self):
        return (f"Shape[color= {self._color},filled= {self._filled}]")


shape = Shape()
print(shape)

