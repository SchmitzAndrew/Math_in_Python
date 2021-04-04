import numpy as np

class Probabilty:
    def __init__(self, A, B, outcomes, possibilities, dependent):
        self.A = A
        self.B = B
        self.outcomes = outcomes
        self.possibilities = possibilities
        self.dependent = dependent

    def chance(self, outcome, possibilities):
        return outcome/ possibilities


    def events(self, A, B, dependent):
        if dependent == True:
            return A + B #dependent
        else:
            return A * B #mutually exclusive



    def conditional_probability(self, A, B, dependent):
        return events(self, A, B, dependent) / B
