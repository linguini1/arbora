# Contains the backend server
__author__ = "Matteo Golin"

# Imports
from utils import load_plants_from_csv, load_environments_from_csv
from classes.forest import Forest
from pprint import pprint

# Constants


# Main
def main():
    plant_dicts = load_plants_from_csv()
    environments = load_environments_from_csv()
    forest = Forest(
        width=100,
        height=100,
        environment=environments["pukaskwa"]
    )
    forest.populate(plant_dicts)


if __name__ == '__main__':
    main()
