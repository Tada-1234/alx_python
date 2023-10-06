"""
This module checks if the object is an instance of, 
or if the object is an instance of a class that inherited, 
the specified class.
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if `obj` is an instance of `a_class` or an instance of a class that
        inherited from `a_class`, otherwise False.

    Note:
        Uses `type(obj).mro()` to iterate over the Method Resolution Order (MRO) of `obj`,
        which includes `obj`'s class, base classes, and the base classes of those base classes,
        etc., checking if any of them are `a_class`.
    """
    if type(obj) is a_class:
        return True
    for cls in type(obj).mro():
        if cls is a_class:
            return True
    return False
