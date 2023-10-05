"""
This module returns true if the object is an instance of a class
"""
def is_same_class(obj, a_class):
    """
    Function checks if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
    
    Args: 
        obj: the object we want to check
        a_class: the class we want to check against

    Returns:
        bool: True if an instance and false if not
    """
    if type(obj) is a_class: #Check if its an instance a class
        return True
    
    for cls in type(obj).mro(): #Check if its an instance of an inherited class
        if cls is a_class: #Checks if its a class
            return True
    return False
