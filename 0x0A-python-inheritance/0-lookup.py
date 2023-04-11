#!/usr/bin/python3
""" creates list of available attributes and methods of lookup object."""


def lookup(obj):
    """ Returns a list of available attributes and methods of the object."""
    return dir(obj)
