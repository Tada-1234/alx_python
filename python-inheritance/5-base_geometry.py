"""
This module creates a class with a method that raises an exception
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
