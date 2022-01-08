import numpy as np


def crossover(chromosome1, chromosome2):
    child1 = None
    child2 = None
    # Make crossover here

    child1.set_origin("crossover")
    child2.set_origin("crossover")
    return child1, child2

def mutate(chromosome):
    # Mutate chromosome here
    return chromosome

def repair(chromosome):
    # Repair chromosome here
    return chromosome

def compute_fitness(chromosome):
    y = chromosome.y
    a = chromosome.model.locations["demand"]
    
    # Calculate fitness value of chromosome here
    fitness = np.sum(a * y)
    chromosome.set_fitness(fitness)

    return fitness

def create_mating_pool(population):
    # Create a mating pool from the current population
    return mating_pool

def next_generation(current_population):
    return next_population

def evaluate(chromosome):
    chromosome.decode()

    if chromosome.needs_repair():
        # Repair the chromosome if needed
        repair(chromosome)

    compute_fitness(chromosome)
        


