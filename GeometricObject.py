## Inherit Practice ## 
import math

# -------------------------------- #  Setting GeometricObject
class GeometricObject : 
    def __init__(self, color = "green", filled = True) :
        self.__color = color
        self.__filled = filled

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color
    
    def isFilled(self):
        return self.__filled
    
    def setFilled(self, Filled):
        self.__filled = Filled

    def __str__(self):
        return " color : " + self.__color + \
            " and filled " + str(self.__filled)
    
# -------------------------------- #  Setting Circle
class Circle(GeometricObject):
    def __init__(self, radius):
        GeometricObject.__init__(self)
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius 

    def getRadius(self):
        return self.__radius
    
    def getArea(self):
        return (self.__radius**2) * math.pi

    def getDiameter(self):
        return self.__radius * 2

    def getPerimeter(self):
        return self.getDiameter * math.pi

    def printCircle(self):
        print(self.__str__() + " radius : "
              + str(self.__radius)) 

# -------------------------------- #  Setting Circle
class Rectangle(GeometricObject):
    def __init__(self, width = 1, height = 1):
        super.__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__height * self.__width
    
    def getPerimeter(self):
        return (self.__height + self.__width) * 2 
    


def main():
    circle = Circle(1.5)
    print(circle.getArea())

main()