"""
This module creates a square class
"""
class Square:
    """ 
    Square Class
    
    A Square class that defines a square by its size and allows calculation of its area.
    
    Attributes:
        __size (int): The size of the square, set as a private attribute.
        
    Methods:
        area: Returns the area of the square.
    """
    
    def __init__(self, size=0):
        """
        The constructor for Square class.
        
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

    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        
        return(self.__size*self.__size)
