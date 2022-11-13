# Contains the backend server
__author__ = "Matteo Golin"

# Imports
from utils import load_plants_from_csv
from pprint import pprint

# Constants


# Main
def main():
    plants = load_plants_from_csv()
    pprint(plants)

if __name__ == '__main__':
    main()
