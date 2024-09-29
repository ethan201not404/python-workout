#!/usr/bin/env python3

"""Solution for chapter 9, Execise 39: Ice Cream Bowl."""


class Scoop():
    """Class representing a single scoope of ice cream.
    The attribute is a flavor, string.
    """

    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    """Class representing a single Bowl.
    It contains a list of Scoops.
    """

    def __init__(self):
        # Note - it scoop did not pass as contstructor positional argrument.
        self.scoops = []

    def add_scoops(self, *new_scoops):
        """Add more scoops to bowl.
        *new_scoops a tuple of all scoops to add.
        """
        for scoop in new_scoops:
            self.scoops.append(scoop)

    def __repr__(self) -> str:
        """Overwrite the repr fucntion using join.
        invoking it on a generator expression, which you can think of 
        as a lazy-evaluating version of a list comprehension.
        crates a string via str.join()
        """
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop("chocolate")
s2 = Scoop("vanilla")

b = Bowl()
b.add_scoops(s1, s2)

print(b)
