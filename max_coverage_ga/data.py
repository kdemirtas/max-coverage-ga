class Settings:
    def __init__(self, input_settings):
        self.N_LOC_DEMAND = input_settings["n_locations_demand"]
        self.N_LOC_FACILITY = input_settings["n_locations_possible_facility"]
        self.MAX_DISTANCE = input_settings["max_coverage_distance"]
        self.MAX_FACILITIES = input_settings["max_facilities"]
        self.POP_SIZE = input_settings["ga_settings"]["population_size"]
        self.P_MUTATE = input_settings["ga_settings"]["mutation_probability"]
        self.MAX_GEN = input_settings["ga_settings"]["maximum_generations"]


class Location:
    def __init__(self, index, info, demand, capacity, locations_reachable):
        self.index = index
        self.info = info
        self.demand = demand
        self.capacity = capacity
        self.locations_reachable = locations_reachable
        self.is_facility = False


    def make_facility(self):
        self.is_facility = True
