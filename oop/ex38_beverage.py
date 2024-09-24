#!/usr/bin/env python3

"""Solution to chapter 9, exercise 38 Berverage class."""


class Beverage():
    """Beverage class taking name and temperature as attribute."""

    def __init__(self, name, temperature="75"):
        self.name = name
        self.temperature = temperature


def create_beverage():
    """Create a list of Beverage and print out."""

    beverages = [Beverage("coke", "0")]
    beverages.append(Beverage("tea"))
    for berverage in beverages:
        print(f"beverage: {berverage.name}; temperature: {berverage.temperature}")


create_beverage()
