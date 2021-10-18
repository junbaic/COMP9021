# Written by *** for COMP9021

# Defines:
# - a class: DarkCorridor, implementing 1 special method
# - another class: Pacer, implementing 3 special methods
#   and (at least) 2 extra methods:
#   * pace()
#   * now_here_in_dark_corridor()
# - a function: compare_stress(), that takes two Pacer objects
#   as arguments.

# Uses the Unicode characters of code point 9654, 9664 and 11036.

from itertools import cycle, chain, islice


# INSERT YOUR CODE HERE
class DarkCorridorError(Exception):
    pass


class DarkCorridor:
    def __init__(self, length):
        self.length = length
        if length <= 0:
            raise DarkCorridorError("The length of the corridor should be strictly positive")

    def __repr__(self):
        return f"DarkCorridor({self.length})"

    def __str__(self):
        return f" {chr(11036)}" * self.length


class Pacer:
    def __init__(self, name, Corridor):
        self.name = name
        self.Corridor = Corridor
        self.len = 0

    def __repr__(self):
        return f"Pacer('{self.name}', {self.Corridor.__repr__()})"

    def __str__(self):
        return f"{self.name} in {self.Corridor.__str__()}"

    def pace(self, num):
        self.len = self.len + num

    def now_here_in_dark_corridor(self):
        x, y = divmod(self.len, self.Corridor.length)
        print(f" {chr(11036)}" * (self.Corridor.length - y - 1) + f" {chr(9664)}" + f" {chr(11036)}" * y) \
            if x % 2 == 1 else \
            print(f" {chr(11036)}" * y + f" {chr(9654)}" + f" {chr(11036)}" * (self.Corridor.length - y - 1))


def compare_stress(pacer1, pacer2):
    a = "step" if pacer1.len <= 1 else "steps"
    b = "step" if pacer2.len <= 1 else "steps"
    if pacer1.len == pacer2.len:
        print(f"{pacer1.name} and {pacer2.name} are both as stressed ({pacer1.len} {a}).")
    elif pacer1.len > pacer2.len:
        print(f"{pacer1.name} ({pacer1.len} {a}) is more stressed than {pacer2.name} ({pacer2.len} {b}).")
    else:
        print(f"{pacer2.name} ({pacer2.len} {b}) is more stressed than {pacer1.name} ({pacer1.len} {a}).")
