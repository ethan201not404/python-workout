#!/usr/bin/env python3

"""Solution for chapter 9, Execise 40: Ice Cream Bowl with Limit."""

SCOOPS_LIMIT = 2


class Scoop():
    """Scoop class with the flavor"""
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl():
    """Bowl contains a list of Scoop."""
    # class attribute before object __init__
    # python doesn't have constants
    max_scoops = SCOOPS_LIMIT

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):

        # refer to class attribue
        if len(self.scoops) >= Bowl.max_scoops:
            raise Exception(f"reached the bowl limit {Bowl.max_scoops}")
        for scoop in new_scoops:
            self.scoops.append(scoop)


s1 = Scoop("apple")
s2 = Scoop("oringe")
s3 = Scoop("pair")

bowl = Bowl()
bowl.add_scoops(s1, s2)
bowl.add_scoops(s3)
