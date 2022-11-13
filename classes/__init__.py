# Contains classes necessary for forest simulation
__author__ = "Matteo Golin"

# Imports
from dataclasses import dataclass

# Constants
DataRange = tuple[int, int]


# Plant Class
class Plant:

    """
    Represents a general plant structure with attributes to decide growth, lifespan, etc.

    Growth rate is unitless.
    Max height is in metres.
    Shade tolerance is unitless.
    Precipitation preference is in millimetres.
    Temperature preference is in degrees celsius.
    Seed radius is in metres.
    Seed production time is in years.
    Lifespan is assigned in years and given in months.
    """

    def __init__(
            self,
            plant_type: str,
            name: str,
            growth_rate: float,
            max_height: float,
            shade_tol: float,
            precip_pref: DataRange,
            temp_pref: DataRange,
            seeds_produced: int,
            seed_radius: float,
            seed_production: float,
            lifespan: int,
    ):
        self.type: str = plant_type
        self.name: str = name
        self.growth_rate: float = max_height/12 *(lifespan - seed_production -1)
        self.max_height: float = max_height
        self.shade_tol: float = shade_tol
        self.precip_pref: DataRange = precip_pref
        self.temp_pref: DataRange = temp_pref
        self.seeds_produced: int = seeds_produced
        self.seed_radius: float = seed_radius
        self.seed_production: float = seed_production
        self.lifespan: int = lifespan * 12  # In months

    def grow(self) -> None:
        pass

    def __repr__(self):
        return f"{self.name}"


# Environment class
@dataclass
class Environment:

    name: str
    temperatures: list[int]
    precipitation: list[float]
