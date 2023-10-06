"""
6-Rectangle.py:
This module creates a class that inherits from another class
"""
class Rectangle(BaseGeometry):
    """
    This class test the variable
    
    Args:
        __width: a private width value
        __height: a private height value

    Attributes:
        __width: a private width value
        __height: a private height value
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
