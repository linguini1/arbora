# Hosts the forest class to simulate the forest area
__author__ = "Matteo Golin"

# Imports
import random
import typing
from utils import create_plant, PlantDict
from classes import Plant, Environment

# Constants


# Forest class
class Forest:

    """Represents the area of forest to be simulated."""

    def __init__(self, environment: Environment, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.map: list[list[Plant]] = [[None for _ in range(width)] for _ in range(height)]  # Initial 100mx100m forest
        self.environment: Environment = environment

    def populate(self, plants: list[PlantDict]) -> None:

        """Populates the forest with a random distribution of plants to cover 10% of the forest area."""

        area = self.width * self.height
        num_plants = len(plants)
        of_each = int(0.1 * area) // num_plants  # How many of each plant
        print(area, num_plants, of_each)

        # Generate enough unique points so of_each number of each plant can be added
        points = set(
            (
                random.randint(0, self.width - 1),
                random.randint(0, self.height - 1)
            ) for _ in range(of_each * num_plants)
        )

        # Continue creating points until enough are made
        while len(points) < of_each * num_plants:
            points.add((random.randint(0, self.width - 1), random.randint(0, self.height - 1)))

        # Get of_each number of coordinates for each plant type and plant the plant at that spot on the graph
        for _ in range(0, of_each * num_plants, of_each):
            for point in list(points)[_:_ + of_each]:
                x, y = point
                self.map[y][x] = create_plant(plants[_ // of_each])  # Index of 0 to num_plants
