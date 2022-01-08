import numpy as np

from .operators import *


class Chromosome:
    """
    Chromosome is an M + N sized numeric array, where M is thenumber of potential facilitiy
    locations and N is the number of demand locations. The first M elements are binary and
    indicate whether or not a facility is opened at the corresponding index location. The next 
    N elements are numeric and hold the index of the facility location the demand is being served from.
    -1 value indicates that location at that index is not served by any facility.
    """
    def __init__(self, model, genotype=None, create_type="default"):
        """
        Creates a chromosome instance with the model data according to the create_type.
        N: number of demand locations
        M: possible number of locations for facilities to be located, i.e, the size of the numpy array.
        K: maximum number of facilities allowed to be open.
        create_type: type of creation. Defaults to random. Other options are 'heuristic', 'top_capacity', 'top_demand'.
        """
        # Parameters
        self.model = model
        self.N = model.settings.N_LOC_DEMAND
        self.M = model.settings.N_LOC_FACILITY
        self.K = model.settings.MAX_FACILITIES

        # Genetic representation
        self.genotype = genotype
        self.origin = None
        self.generation = None
        self.facility_indexes = None
        self.fitness = 0.0

        # Mathematical model decision variables
        self.x = np.zeros(self.M)
        self.z = np.zeros([self.N, self.M])
        self.y = np.zeros(self.N)
        
        if create_type == "default":
            pass

        if create_type == "random":
            # Create chromosome randomly.      
            self.genotype = np.negative(np.ones(self.M + self.N))  
            self.facility_indexes = np.random.choice(range(self.M), self.K, replace=False)
            self.genotype[self.facility_indexes] = 1
            self.origin = "default"
            self.generation = 0

            for i in self.facility_indexes:
                # Self assign demand location i if a facility is opened at that location.
                self.genotype[i + self.M] = i
                reachable_indexes = model.locations_list[i].locations_reachable

        elif create_type == "crossover":
            self.origin = "crossover"

        elif create_type == "mutation":
            self.origin = "mutation"

        elif create_type == "repair":
            self.origin = "repair"

    def set_generation(self, generation):
        self.generation = generation

    def set_fitness(self, fitness):
        self.fitness = fitness

    def needs_repair(self):
        """
        Checks the chromosome for infeasibility and returns True if repair is needed.
        Returns False otherwise.
        """
        # x feasibility


        # y feasibility


        # z feasibility


        # capacity feasibility


        result = False

        return result

    def decode(self):
        """
        Decodes the array representation of the chromosome and provides
        a user-friendly solution description.
        """
        self.x[self.facility_indexes] = 1
        genotype_assignment_portion = self.genotype[self.M:]
        for i, val in enumerate(genotype_assignment_portion):
            if val == -1:
                self.z[i] = 0
            elif val >= 0:
                j = int(val)
                self.y[j] = 1
                self.z[j][j] = 1

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

    def next_generation(self):
        pass


    def __str__(self):
        pass