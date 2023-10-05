"""
This module creates a class that inherits from another class
"""
class BaseGeometry:
    """
    This class raises exceptions
    """
    def area(self):
        """
        Function raises an exception
    
        Args: 
            self: our class

        Returns:
            Exception
        """
        raise Exception("area() is not implemented")
   
    def integer_validator(self, name, value):
        """
        Function raises an exception
    
        Args: 
            self: our class
            name: the name of data we are passing
            value: value of the data(numerical)

        Returns:
            Exception: if the variable is not valid
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        else:
            return

class Rectangle(BaseGeometry):
    """
    This class test the variable
    """
    def __init__(self, width, height):
        """
        Function checks the variables
    
        Args: 
            self: our class
            width: the width of the rectangle
            height: the height of the rectangle

        Returns:
            nothing
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height