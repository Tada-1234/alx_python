"""
This module is used to create a square class
"""

class Square:
    """
    Square Class
    
    A Square class that defines a square by its size.
    
    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.
        
        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size
