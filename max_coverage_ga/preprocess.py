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

def parse_distance_matrix(filename, sheet_name):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    files_dir = os.path.join(root_dir, "files")
    file_path = os.path.join(files_dir, filename)
    distances = pd.read_excel(file_path, sheet_name).values
    return distances

def get_coverage_matrix(distances, max_distance):
    pass

def test():
    distances = parse_distance_matrix("Distance Matrix.xlsx", "distances")
    print(distances)
    print("Done")
    

if __name__ == "__main__":
    test()