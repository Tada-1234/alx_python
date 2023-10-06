"""
This module creates an empty class
"""
class BaseGeometry:
    """
    Overrides dir()

    Args:
        self: the class itself

    Returns:
        nothing
    """
    def __dir__(self, my_class):
        attributes = my_class.__dir__()  # Get the default dir()
        filtered_attributes = [attr for attr in attributes if attr != '__init_subclass__']
        return filtered_attributes
