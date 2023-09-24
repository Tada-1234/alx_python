"""
THIS MODULE CREATES A SQUARE CLASS
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
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return(self.__size*self.__size)
    @property
    def size(self):
        """
        The size property to get the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return(self.__size)
    @size.setter
    def size(self, value):
        """
        Setter for size attribute.
        
        Parameters:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
