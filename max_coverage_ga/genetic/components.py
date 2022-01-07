import numpy as np


class Chromosome:
    """
    Chromosome is a binary numpy array with size equal to the number of possible facility locations.
    1 at index i means a facility is opened at location i, 0 means otherwise.
    """
    def __init__(self):
        self.array
    def __str__(self):
        pass


class Population:
    """
    Population is a collection of chromosome instances iterating through generations according to 
    the genetic algorithm operators until a termination condition is reached.
    """
    def __init__(self, initial_population):
        self.population = initial_population
        self.diversity = None
        self.generation = 0
        self.terminate = False

    def __str__(self):
        pass