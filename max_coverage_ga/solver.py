from max_coverage_ga.genetic.components import Chromosome, Population
from max_coverage_ga.genetic.operators import *


def solve(model):
    pop_size = model.settings.POP_SIZE
    n_loc_demand = model.settings.N_LOC_DEMAND
    n_loc_faciility = model.settings.N_LOC_FACILITY
    max_facility = model.settings.MAX_FACILITIES
    p_cross = model.settings.P_CROSS
    p_mutate = model.settings.P_MUTATE
    
    # Initialize population 
    initial_pop = []
    for c in range(n_loc_faciility, max_facility):
        initial.append(Chromosome(n_loc_faciility, max_facility, create_type="random"))

    pop = Population(initial_pop)

    while not terminate:
        next_generation(pop)
