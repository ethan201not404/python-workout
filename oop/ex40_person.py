#!/usr/bin/env python3

"""Solution for chapter 9, Execise 40: Person Class attribute."""


class Person():

    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1


p1 = Person("David")
p2 = Person("Jenny")

print(p1.population)
print(Person.population)
