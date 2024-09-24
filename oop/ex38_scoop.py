#!/usr/bin/env python3

"""Solution to chapter 9, exercise 38: scoop"""


class Scoop():
    """Class representing a single scoop of ice cream.
    The attribute is flavor, a string.
    """

    def __init__(self, flavor):
        self.flavor = flavor


def create_scoop():
    """Function that creates scoops and put them in a list
    and printout the flavors.
    """

    scoops = [Scoop("apple"), Scoop("pair")]
    for scoop in scoops:
        print(scoop.flavor)


create_scoop()
