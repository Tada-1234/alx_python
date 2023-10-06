"""
This module creates a class that inherits from another class
"""
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
