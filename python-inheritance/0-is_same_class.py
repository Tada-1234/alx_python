"""
This module returns true if the object is an instance of a class
"""
def is_same_class(obj, a_class):
    """
    Function checks if its an instance of a class
    
    Args: 
        obj: the object we want to check
        a_class: the class we want to check against

    Returns:
        bool: True if an instance and false if not
    """
    if type(obj) is a_class:
        return True
