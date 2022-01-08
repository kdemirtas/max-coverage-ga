import numpy as np

from data import Location


def get_coverage_matrix(distances, max_distance):
    coverage_matrix = np.where(distances <= max_distance, 1, 0)
    return coverage_matrix


class Model:
    def __init__(self, model_data={}):
        self.settings = model_data["settings"]
        self.locations = model_data["locations"]
        self.locations_list = []
        self.distances = model_data["distances"]
        self.coverage = get_coverage_matrix(self.distances, self.settings.MAX_DISTANCE)
        self._initialize_model()

    def _initialize_model(self):
        info = self.locations["info"]
        demand = self.locations["demand"]
        capacity = self.locations["capacity"]
        
        for i in range(self.settings.N_LOC_FACILITY):
            row = self.coverage[i]
            locations_reachable = np.where(row == 1)
            loc = Location(i, info[i], demand[i], capacity[i], locations_reachable)
            self.locations_list.append(loc)



class Solution:
    def __init__(self):
        pass

