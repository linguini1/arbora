# Contains utils for forest simulation
__author__ = "Matteo Golin"

# Imports
import csv
import typing
from os import listdir
import random
from os.path import isfile, join
from classes import Plant, Environment, DataRange

# Constants
PLANTS_CSV = "./resources/plants.csv"
ENVIRONMENTS = "./resources/environments"
PlantDict = dict[str, typing.Any]


# Functions
def parse_temperature(temperature_range: str) -> DataRange:

    """Returns the temperature range string as a tuple of the minimum and maximum values."""

    data_range = temperature_range.split("to")
    return int(data_range[0]), int(data_range[1])


def parse_precipitation(precip_range: str) -> DataRange:

    """
    Returns the temperature range string as a tuple of the minimum and maximum values scaled to
    precipitation per month.
    """

    data_range = precip_range.split("-")
    return int(data_range[0]) // 12, int(data_range[1]) // 12


def create_plant(plant_dict: PlantDict) -> Plant:

    """Returns a plant object created from a CSV row."""

    return Plant(
        plant_type=plant_dict["Plant type"],
        name=plant_dict["Plant Name"],
        growth_rate=float(plant_dict["Growth Rate"]),
        max_height=float(plant_dict["Maximum Height"]),
        shade_tol=float(plant_dict["Shade tolerance"]),
        precip_pref=parse_precipitation(plant_dict["Precipitation Preference"]),
        temp_pref=parse_temperature(plant_dict["Temperature Preference"]),
        seeds_produced=int(plant_dict["Seeds produced"]),
        seed_radius=int(float(plant_dict["Seed radius"])),
        seed_production=float(plant_dict["Seed production time"]),
        lifespan=int(plant_dict["Lifespan"]),
    )


def row_to_dict(plant_csv_row: list[str], headers: list[str]) -> PlantDict:

    """
    Returns the CSV row converted to a dictionary object where the column header is the key and
    the column value is the value.
    """

    row_dict = {}
    for _ in range(len(headers)):
        row_dict.update(
            {headers[_]: plant_csv_row[_]}
        )

    return row_dict


def load_plants_from_csv() -> list[PlantDict]:

    """Returns a list of plant objects created from the plant database stored in a CSV file."""

    plant_lib = []
    with open(PLANTS_CSV, 'r') as file:
        plants = csv.reader(file)
        headers = next(plants)  # Skip the header line
        for plant in plants:
            plant_dict = row_to_dict(plant, headers)
            plant_lib.append(plant_dict)

    return plant_lib


def load_environments_from_csv() -> dict[str, Environment]:

    """Returns a dictionary where keys of environment names are mapped to Environment objects."""

    # Find all environment csv files in the environments directory
    environment_files = []
    for file in listdir(ENVIRONMENTS):
        file_path = join(ENVIRONMENTS, file)
        if isfile(file_path):
            environment_files.append(file)

    # Store environments in dictionary
    env_dict = {}
    for env in environment_files:

        temperatures = []  # Storage for monthly temperature
        precipitation = []  # Storage for monthly precipitation
        name = env.split(".")[0]  # Remove file extension

        # Read each environment csv
        with open(f"{ENVIRONMENTS}/{env}", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers
            for row in reader:
                temperatures.append(int(row[1]))
                precipitation.append(float(row[2]))

            # Create Environment object
            environment = Environment(
                name=name,
                temperatures=temperatures,
                precipitation=precipitation,
            )

            # Add Environment object to dict
            env_dict.update({name: environment})

    return env_dict


def generate_unique_points(x1: int, x2: int, y1: int, y2: int, n: int) -> list[tuple[int, int]]:

    """Returns a list of n unique (x, y) coordinate pairs within the specified x and y range."""

    # Generate enough unique points so of_each number of each plant can be added
    points = set(
        (
            random.randint(x1, x2),
            random.randint(y1, y2)
        ) for _ in range(n)
    )

    # Continue creating points until enough are made
    while len(points) < n:
        points.add((random.randint(x1, x2), random.randint(y1, y2)))

    return list(points)