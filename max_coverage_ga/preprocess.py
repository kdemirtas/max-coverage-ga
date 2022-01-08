import json
import os
import pandas as pd
import numpy as np

from data import Location, Settings
import model

def create_model(filename):
    with open(filename) as fp:
        inp = json.load(fp)
    
    input_settings = inp["settings"]
    # Create the model parameters and genetic algorithm settings
    settings = model.Settings(input_settings)

    # Create the locations dictionary with keys equal to location indices and
    # values holding Location instances

    # TODO Consider reading the locations from csv
    locations = inp["locations"]

    mod = model.Model(settings, locations)
    return mod

def parse_distances(filename, sheet_name):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    files_dir = os.path.join(root_dir, "files")
    file_path = os.path.join(files_dir, filename)
    distances = pd.read_excel(file_path, sheet_name).values
    return distances

def parse_locations(filename):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    files_dir = os.path.join(root_dir, "files")
    file_path = os.path.join(files_dir, filename)
    info = _parse_info(file_path)
    demand = _parse_demand(file_path)
    capacity = _parse_capacity(file_path)
    locations = {
        "info": info,
        "demand": demand,
        "capacity": capacity
    }
    return locations

def _parse_demand(file_path, sheet_name="demand"):
    demand = pd.read_excel(file_path, sheet_name=sheet_name).values.flatten()
    return demand

def _parse_capacity(file_path, sheet_name="capacity"):
    capacity = pd.read_excel(file_path, sheet_name=sheet_name).values.flatten()
    return capacity

def _parse_info(file_path, sheet_name="info"):
    info = pd.read_excel(file_path, sheet_name=sheet_name).values.flatten()
    return info

def get_coverage_matrix(distances, max_distance):
    coverage = np.where(distances <= max_distance, 1, 0)
    return coverage 

def test():
    distances = parse_distances("Distance Matrix.xlsx", "distances")
    locations = parse_locations("Project Data.xlsx")
    coverage = get_coverage_matrix(distances, 20)
    print(distances)
    print(locations)
    print(coverage)
    print("Done")
    

if __name__ == "__main__":
    test()