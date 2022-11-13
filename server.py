# Contains the backend server
__author__ = "Matteo Golin"

# Imports
from utils import load_plants_from_csv, load_environments_from_csv
from classes.forest import Forest
from flask import Flask

# Constants
def print_row(row):
    print([_.name[0] if _ else " " for _ in row])

# Main
app = Flask(__name__)

def main():
    plant_dicts = load_plants_from_csv()
    environments = load_environments_from_csv()
    forest = Forest(
        width=20,
        height=20,
        environment=environments["pukaskwa"],
        plants=plant_dicts
    )
    forest.populate()
    for row in forest.map:
        print_row(row)
    for _ in range(40):
        for month in range(12):
            forest.increment(month)

            for row in forest.map:
                print_row(row)
            print()


if __name__ == '__main__':
    main()
