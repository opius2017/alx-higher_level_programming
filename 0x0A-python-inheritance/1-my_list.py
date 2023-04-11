#!/usr/bin/python3
""" MyList is a subclass of the built-in list class. """


class MyList(list):
    """ This class inherits all the attributes and methods of list """

    def print_sorted(self):
        """ Prints the list in ascending order. """
        print(sorted(self))
