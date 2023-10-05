"""
This module creates a class with a method that raises an exception
"""
class BaseGeometry:
    """
    Function raises an exception
    
    Args: 
        self: our class

    Returns:
        Exception
    """
    def area(self):
        raise Exception("area() is not implemented")
