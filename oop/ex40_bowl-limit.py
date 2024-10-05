#!/usr/bin/env python3

"""Solution for chapter 9, Execise 40: Ice Cream Bowl with Limit."""

LIMIT = 2


class Scoop():
    """Scoop class with the flavor"""
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    """Bowl contains a list of Scoop."""

    def __init__(self, limit=LIMIT):
        self.scoops = []
        self.limit = limit

    def add_scoops(self, *new_scoops):

        if len(self.scoops) >= self.limit:
            raise f"reached the limit {self.limit}"
        for scoop in new_scoops:
            self.scoops.append(scoop)


s1 = Scoop("apple")
s2 = Scoop("oringe")
s3 = Scoop("pair")

bowl = Bowl()
bowl.add_scoops(s1, s2)
# bowl.add_scoops(s3)
