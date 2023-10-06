"""
This module returns true if the object is an instance of a class
"""
def inherits_from(obj, a_class):
    """
    Function checks if its an instance of a class

    Args: 
        obj: the object we want to check
        a_class: the class we want to check against

    Returns:
        bool: True if an instance and false if not
    """
    for cls in type(obj).mro():
        if cls is a_class:
            return True
    return False
