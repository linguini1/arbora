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
            growth_rate: float,  # Decided was useless
            max_height: float,
            shade_tol: float,
            precip_pref: DataRange,
            temp_pref: DataRange,
            seeds_produced: int,
            seed_radius: float,
            seed_production: float,
            lifespan: int,
    ):

        # Data from file
        self.type: str = plant_type
        self.name: str = name
        self.growth_rate: float = max_height / 12 * (lifespan - seed_production - 1)
        self.max_height: float = max_height
        self.shade_tol: float = shade_tol
        self.precip_pref: DataRange = precip_pref
        self.temp_pref: DataRange = temp_pref
        self.seeds_produced: int = seeds_produced
        self.seed_radius: float = seed_radius
        self.seed_production: float = seed_production
        self.lifespan: int = lifespan * 12  # In months

        # Changing data
        self.age: int = 0
        self.height: float = 0
        self.alive = True
        self.seed_clock = 0
        self.fertile = False

    def grow(self, temperature: int, precipitation: float) -> None:

        """Allows the plant to grow each monthly time step."""

        month_gr = self.growth_rate  # This month's growth rate (allows environmental factors)

        # Reduce GR if temperature is not in preferred range
        if not self.temp_pref[0] <= temperature <= self.temp_pref[1]:
            month_gr *= 0.5

            # How much out of range is the temperature
            out_of_range = max(self.temp_pref[0] - temperature, temperature - self.temp_pref[1])
            if out_of_range >= 3:  # 3 degree tolerance
                self.alive = False  # Plant dies

        # Reduce GR if precipitation is not in preferred range
        if not self.precip_pref[0] <= precipitation <= self.precip_pref[1]:
            month_gr *= 0.5

            # How much out of range is the precipitation
            out_of_range = max(self.precip_pref[0] - precipitation, precipitation - self.precip_pref[1])
            if out_of_range >= 41:  # 41mm tolerance
                self.alive = False

        # Don't grow past max height
        if self.height + month_gr < self.max_height:
            self.height += month_gr
        else:
            self.height = self.max_height
            self.seed_clock += 1

        # If we have waited the seed production time, show that the plant is fertile
        if self.seed_clock == self.seed_production:
            self.fertile = True  # Seeds will be planted in seed radius next turn

        self.age += 1  # Increase age

    def reset_fertility(self):

        """Resets the plant's seed clock and fertility status after a batch of seeds are planted."""

        self.fertile = False
        self.seed_clock = 0

    def __repr__(self):
        return f"{self.name}"


# Environment class
@dataclass
class Environment:

    name: str
    temperatures: list[int]
    precipitation: list[float]
