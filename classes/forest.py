# Hosts the forest class to simulate the forest area
__author__ = "Matteo Golin"

# Imports
import random
import typing
from utils import create_plant, PlantDict, generate_unique_points
from classes import Plant, Environment


# Forest class
class Forest:

    """Represents the area of forest to be simulated."""

    def __init__(self, environment: Environment, plants: list[PlantDict], width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.map: list[list[Plant]] = [[None for _ in range(width)] for _ in range(height)]  # Initial 100mx100m forest
        self.environment: Environment = environment
        self.plants: list[PlantDict] = plants

    def populate(self) -> None:

        """Populates the forest with a random distribution of plants to cover 10% of the forest area."""

        area = self.width * self.height
        num_plants = len(self.plants)
        of_each = int(0.1 * area) // num_plants  # How many of each plant

        # Generate unique points to accommodate each plant type
        points = generate_unique_points(0, self.width -1, 0, self.height - 1, num_plants * of_each)

        # Get of_each number of coordinates for each plant type and plant the plant at that spot on the graph
        for _ in range(0, of_each * num_plants, of_each):
            for point in list(points)[_:_ + of_each]:
                x, y = point
                self.map[y][x] = create_plant(self.plants[_ // of_each])  # Index of 0 to num_plants

    def increment(self, month: int) -> None:

        """Increments the time step by one month."""

        temperature = self.environment.temperatures[month]
        precipitation = self.environment.precipitation[month]

        # Iterate through plants
        for y in range(self.height):
            for x in range(self.width):
                plant = self.map[y][x]
                if plant:  # Make sure there is a plant in cell
                    # Check for death
                    if not plant.alive:
                        self.map[y][x] = None  # Delete dead plant
                    else:
                        # Check for fertility
                        if plant.fertile:
                            # Create seeds
                            points = generate_unique_points(
                                max(0, x - plant.seed_radius), min(x + plant.seed_radius, self.width - 1),
                                max(0, y - plant.seed_radius), min(y + plant.seed_radius, self.height - 1),
                                plant.seeds_produced
                            )

                            # Plant all new seeds
                            for point in points:
                                point_x, point_y = point
                                cell = self.map[point_y][point_x]
                                if not cell:

                                    # Plant a plant of the same type as parent
                                    for plant_type in self.plants:
                                        if plant_type["Plant Name"] == plant.name:
                                            self.map[point_y][point_x] = create_plant(plant_type)
                                            break

                            plant.reset_fertility()

                        # Grow plant
                        plant.grow(temperature, precipitation)

    def json(self) -> dict:

        """Returns one dimensional array representation of forest."""

        representation = []
        for y in range(self.height):
            for x in range(self.width):
                plant = self.map[y][x]
                if plant:
                    representation.append(plant.json())
                else:
                    representation.append(None)

        return {"forest": representation}
