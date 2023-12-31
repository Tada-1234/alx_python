"""
This module creates a square
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    This class creates a square from a rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Function initiates and counts objects

        Args:
            self: Our Class
            size: side of the square
            x: i dont know what this is
            y: i dont know what this is
            id: Number of Objects

        Returns:
            Nothing/error
        '''
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__x = x
        self.__y = y

    def __str__(self):
        '''
        Overrides __str__ method so that the print function prints something new

        Args:
            self: our class

        Returns:
            the new way of printing
        '''
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    @property
    def size(self):
        """
        function gets private/protected values

        Args:
            self: the class
        
        Returns:
            the private/protected value
        """
        return self.width
    
    @size.setter
    def size(self, size):
        """
        function sets private/protected values

        Args:
            self: the class
            width: width of the rectangle
        
        Returns:
            nothing
        """
        self.width = size
