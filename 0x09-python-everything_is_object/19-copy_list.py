#!/usr/bin/python3


def copy_list(clst):
    """
    This function takes a list as input and returns a copy of the input list.
    If the input is not a list, it returns the input as it is.
    """
    return clst.copy() if isinstance(clst, list) else clst
