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

    """
    Overrides dir() 

    Args:
        self: the class itself
    Returns:
        nothing
    """
    def __dir__(self):
        attributes = super().__dir__()  # Get the default dir()
        filtered_attributes = [attr for attr in attributes if attr != '__init_subclass__']
        return filtered_attributes
