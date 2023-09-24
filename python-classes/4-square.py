"""
This module creates a square class
"""
class Square:
    """ 
    Square Class
    
    A Square class that defines a square by its size and provides
    a method to calculate its area.
    
    Attributes:
        __size (int): Private instance attribute to store the size of the square.
    """
    def __init__(self, size=0):
        """ 
        Constructor for the Square class.
        
        Parameters:
            size (int, optional): The size of the square. Defaults to 0.
            
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):       
        """ 
        Calculate and return the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return(self.__size*self.__size)
    @property
    def size(self):
        """ 
        Getter for the size attribute.
        
        Returns:
            int: The size of the square.
        """
        return(self.__size)
    @size.setter
    def size(self, value):
        """ 
        Setter for the size attribute.
        
        Parameters:
            value (int): The new size of the square.
            
        Raises:
            TypeError: If the new size is not an integer.
            ValueError: If the new size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def my_print(self):
        """
        my-print prints the square using '#' characters.
        
        If the size is 0, prints an empty line.
        """
        if self.__size > 0:
            for x in range(0, self.__size):
                for y in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
