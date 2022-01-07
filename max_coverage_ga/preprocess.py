import json
import os

from .import data
from .import model

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
