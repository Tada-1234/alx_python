"""
This module checks if the object is an instance of, 
or if the object is an instance of a class that inherited from, 
the specified class.
"""
def is_same_class(obj, a_class):
    """
    The function checks if the object is an instance of the specified class or 
    an instance of a class that inherited from the specified class.
    
    Args: 
        obj (object): The object to be checked.
        a_class (type): The class (or a tuple of classes) to check against.
    
    Returns:
        bool: Returns True if 'obj' is an instance of 'a_class' or an instance
              of a class that inherited from 'a_class', otherwise False.
    """
    if type(obj) is a_class: # Check if 'obj' is an exact instance of 'a_class'
        return True

     # Check if 'obj' is an instance of a class that inherited from 'a_class'
    for cls in type(obj).mro():
        if cls is a_class:
            return True
    return False
