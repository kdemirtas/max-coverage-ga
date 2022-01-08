from preprocess import create_model
from model import Solution


def solve(model):
    pop_size = model.settings.POP_SIZE
    n_loc_demand = model.settings.N_LOC_DEMAND
    n_loc_faciility = model.settings.N_LOC_FACILITY
    max_facility = model.settings.MAX_FACILITIES
    p_mutate = model.settings.P_MUTATE
    status = -1
    
    # Initialize population 
    initial_pop = []
    for c in range(n_loc_faciility, max_facility):
        initial.append(Chromosome(n_loc_faciility, max_facility, create_type="random"))

    pop = Population(initial_pop)

    while not terminate:
        next_generation(pop)

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

