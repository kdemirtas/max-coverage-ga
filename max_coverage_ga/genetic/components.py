import numpy as np


class Chromosome:
    """
    Chromosome is an M + N sized numeric array, where M is thenumber of potential facilitiy
    locations and N is the number of demand locations. The first M elements are binary and
    indicate whether or not a facility is opened at the corresponding index location. The next 
    N elements are numeric and hold the index of the facility location the demand is being served from.
    """
    def __init__(self, n_loc_faciility, max_facility=0, create_type="default"):
        """
        Creates a chromosome instance with the parameters according to the create_type.
        n_loc_faciility: possible number of locations for facilities to be located, i.e, the size of the numpy array.
        max_facility: maximum number of facilities allowed to be open.
        create_type: type of creation. Defaults to random. Other options are 'heuristic', 'top_capacity', 'top_demand'.
        """
        if create_type == "default" or create_type == "random":
            # Create chromosome randomly.
            pass

        elif create_type == "heuristic":
            pass

        elif create_type == "top_capacity":
            pass

        elif create_type == "top_demand":
            pass


    def needs_repair(self):
        """
        Checks the chromosome for infeasibility and returns True if repair is needed.
        Returns False otherwise.
        """
        return False

    def decode(self):
        """
        Decodes the binary array representation of the chromosome and provides
        a user-friendlu description.
        """
        pass

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