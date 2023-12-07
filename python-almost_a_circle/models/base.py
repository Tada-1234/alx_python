"""
This module holds the number of objects created from the class
"""
class Base:
    """
    This class counts objects
    """
    __nb_objects = 0 #private class attribute

    def __init__(self, id=None):
        """
        Function initiates and counts objects

        Args:
            self: Our Class
            id: Number of Objects

        Returns:
            Nothing
        """
        if id is not None:
            Base.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects
