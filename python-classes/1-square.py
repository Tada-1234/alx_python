"""
This module creates a square class
"""

class Square:
    """ 
    Square Class
    
    A Square class that defines a square object by its size.
    
    Attributes:
        __size (int): Private instance attribute to hold the size of the square.
        
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """ 
        Constructor for Square class.
        
        Initializes a Square object with a given size, which defaults to 0 
        if not provided.
        
        Parameters:
            size (int, optional): The size of the square's side. Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be >= 0")
        if size < 0:
            raise ValueError("size must be an integer")
        
        self.__size = size
