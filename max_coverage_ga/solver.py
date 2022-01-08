import numpy as np

from preprocess import create_model
from model import Solution
from genetic.components import Chromosome, Population
from genetic.operators import *

# Set random seed for reproducible results
np.random.seed(7)

def solve(model):
    pop_size = model.settings.POP_SIZE

    p_mutate = model.settings.P_MUTATE
    status = -1
    
    # Initialize population 
    initial_pop = []
    for c in range(pop_size):
        chromosome = Chromosome(model, create_type="random")
        evaluate(chromosome)
        initial_pop.append(chromosome)

    pop = Population(initial_pop)

    terminate = False
    while not terminate:
        pass

    solution = Solution()
    return status, solution

if __name__ == "__main__":
    

    input_files_dict = {
        "settings": "settings.json",
        "distances": "Distance Matrix.xlsx",
        "locations": "Project Data.xlsx"
    }
    model = create_model(input_files_dict)
    status, solution = solve(model)


    print("Done")

