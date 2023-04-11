#!/usr/bin/python3

class MyList(list):
    """
    MyList is a subclass of the built-in list class. It inherits all the
    attributes and methods of list, and adds a new public instance method
    print_sorted() that prints the list in ascending order.
    """

    def print_sorted(self):
        """ Prints the list in ascending order. """
        print(sorted(self))
