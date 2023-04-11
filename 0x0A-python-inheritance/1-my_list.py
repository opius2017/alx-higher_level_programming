#!/usr/bin/python3

class MyList(list):
    """ MyList is a subclass of the built-in list class. """

    def print_sorted(self):
        """ Prints the list in ascending order. """
        print(sorted(self))
