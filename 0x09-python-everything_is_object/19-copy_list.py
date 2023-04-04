#!/usr/bin/python3

def copy_list(l):
"""
This function takes a list as input and returns a copy of the input list.
If the input is not a list, it returns the input as it is.
"""
return l.copy() if isinstance(l, list) else l
