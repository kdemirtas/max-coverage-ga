class Settings:
    def __init__(self, input_settings):
        self.N_LOC_DEMAND = input_settings["n_locations_demand"]
        self.N_LOC_FACILITY = input_settings["n_locations_possible_facility"]
        self.MAX_DISTANCE = input_settings["max_coverage_distance"]
        self.MAX_FACILITIES = input_settings["max_facilities"]
        self.POP_SIZE = input_settings["ga_settings"]["population_size"]
        self.P_CROSS = input_settings["ga_settings"]["crossover_probability"]
        self.P_MUTATE = input_settings["ga_settings"]["maximum_generations"]


class Location:
    def __init__(self):
        self.info = None
        self.index = None
        self.demand = None
        self.capacity = None
        self.is_facility = False

    def make_facility(self):
        self.is_facility = True
