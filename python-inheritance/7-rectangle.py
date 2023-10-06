"""
This module creates a class that inherits from another class and the print it.
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

    def __dir__(self):
        """
        Overrides dir()
    
        Args:
            self: the class itself
        
        Returns:
            nothing
        """
        attributes = self.__dir__()  # Get the default dir()                                                                                         
        filtered_attributes = [attr for attr in attributes if attr != '__init_subclass__']
        return filtered_attributes
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
    
    def area(self):
        """
        Function calculates area
    
        Args: 
            self: our class

        Returns:
            area: width * height of rectangle
        """
        return (self.__height * self.__width)

    def __str__(self):
        """
        Function prints
    
        Args: 
            self: our class

        Returns:
            String: Rectangle width/height
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
