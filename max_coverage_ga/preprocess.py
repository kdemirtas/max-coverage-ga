import json
import os
import pandas as pd
import numpy as np

from data import Settings
from model import Model

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
FILES_DIR = os.path.join(ROOT_DIR, "files")

def create_model(input_files_dict):
    """
    Parse input files and create the model components and genetic algorithm settings.
    """ 
    model_data = {}

    # Parse settings from json input file -settings.json-
    filename = input_files_dict["settings"]
    input_settings = _parse_settings(filename)
    settings = Settings(input_settings)
    model_data["settings"] = settings

    # Parse locations data from excel input file -Project Data.xlsx-
    filename = input_files_dict["locations"]
    model_data["locations"] = _parse_locations(filename)
    
    # Parse distances from excel input file -Distance Matrix.xlsx-
    filename = input_files_dict["distances"]
    model_data["distances"] = _parse_distances("Distance Matrix.xlsx", "distances")

    model = Model(model_data)
    return model

def _parse_settings(filename):
    file_path = os.path.join(FILES_DIR, filename)
    with open(file_path) as fp:
        inp = json.load(fp)
    
    input_settings = inp["settings"]
    return input_settings


def _parse_distances(filename, sheet_name):
    file_path = os.path.join(FILES_DIR, filename)
    distances = pd.read_excel(file_path, sheet_name, header=None).values
    return distances

def _parse_locations(filename):
    file_path = os.path.join(FILES_DIR, filename)
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
    demand = pd.read_excel(file_path, sheet_name=sheet_name, header=None).values.flatten()
    return demand

def _parse_capacity(file_path, sheet_name="capacity"):
    capacity = pd.read_excel(file_path, sheet_name=sheet_name, header=None).values.flatten()
    return capacity

def _parse_info(file_path, sheet_name="info"):
    info = pd.read_excel(file_path, sheet_name=sheet_name,header=None).values.flatten()
    return info


if __name__ == "__main__":
    test()