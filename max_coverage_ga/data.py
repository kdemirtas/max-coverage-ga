class Settings:
    def __init__(self, settings):
        self.N_LOC_DEMAND = settings["n_locations_demand"]
        self.N_LOC_FACILITY = settings["n_locations_possible_facility"]
        self.MAX_DISTANCE = settings["max_coverage_distance"]
        self.POP_SIZE = settings["ga_settings"]["population_size"]
        self.P_CROSS = settings["ga_settings"]["crossover_probability"]
        self.P_MUTATE = settings["ga_settings"]["maximum_generations"]


class Location:
    def __init__(self):
        self.info = None
        self.index = None
        self.demand = None
        self.capacity = None
        self.is_facility = False

    def make_facility(self):
        self.is_facility = True
