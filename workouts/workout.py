"""
Workout

Our workout classes
"""


import datetime
from typing import List

from workouts.conversions import convert_time


class Workout:
    """
    Workout

    A workout class
    """

    name: str
    date: datetime

    def __init__(self, name: str, date: datetime):
        self.name = name
        self.date = date


class Lift(Workout):
    """
    Lift

    A lifting type of workout
    """

    weights: List[int]
    reps: List[int]
    sets: List[int]

    def __init__(
        self,
        name: str,
        date: datetime,
        weights: List[int],
        reps: List[int],
        sets: List[int],
    ):
        super().__init__(name, date)
        self.weights = weights
        self.reps = reps
        self.sets = sets

    @property
    def total_reps(self) -> int:
        """
        Returns the total number of reps for this lift
        """
        total_reps = 0
        for idx, rep in enumerate(self.reps):
            total_reps += self.sets[idx] * rep
        return total_reps

    @property
    def total_weight(self) -> int:
        """
        Returns the total weight lifted for this lift
        """
        total_weight = 0
        for idx, weight in enumerate(self.weights):
            total_weight += self.sets[idx] * self.reps[idx] * weight
        return total_weight


class Cardio(Workout):
    """
    Cardio

    A cardio type of workout
    """

    times: List[int]
    time_units: List[str]
    speeds: List[int]
    speed_units: List[str]
    resistances: List[int]
    distances: List[int]
    distance_units: List[str]

    def __init__(
        self,
        name: str,
        date: datetime,
        times: List[int],
        time_units: List[str],
        speeds: List[int],
        speed_units: List[str],
        resistances: List[int],
        distances: List[int] = None,
        distance_units: List[str] = None,
    ):
        super().__init__(name, date)
        self.times = times
        self.time_units = time_units
        self.speeds = speeds
        self.speed_units = speed_units
        self.resistances = resistances

        if distance_units:
            self.distance_units = distance_units
        else:
            self.distance_units = self._get_distance_units_from_speed_units()

        if distances:
            self.distances = distances
        else:
            self.distances = self._get_distances_from_speed_and_time()

    def _get_distance_units_from_speed_units(self) -> List[str]:
        """
        Returns the distance units from the speed units
        """
        distance_units = []
        for speed_unit in self.speed_units:
            distance_unit = speed_unit.split("/")[0]
            distance_units.append(distance_unit)
        return distance_units

    def _get_distances_from_speed_and_time(self) -> List[int]:
        """
        Returns the distance from the speed and time
        """
        distances = []

        for idx, speed_unit in enumerate(self.speed_units):
            time_unit = speed_unit.split("/")[1]

            if time_unit != self.time_units[idx]:
                # TODO: Set up logging in the future
                print(
                    f"Units for time ({self.time_units[idx]}) did not match \
                        units from speed ({time_unit})!"
                )
                print(f"Converting time accorrding to speed units ({time_unit})")
                # Convert times and time units to match speed's time units
                self.times[idx] = convert_time(
                    self.times[idx], self.time_units[idx], time_unit
                )
                self.time_units[idx] = time_unit

            distances.append(self.speeds[idx] * self.times[idx])

        return distances


class WorkoutFactory:
    """
    Factory for creating workouts
    """

    @staticmethod
    def create_workout(workout_type: str, **kwargs) -> Workout:
        """
        Creates a workout based on the type of workout
        """
        if workout_type == "lift":
            return Lift(**kwargs)
        elif workout_type == "cardio":
            return Cardio(**kwargs)
        else:
            raise ValueError("Workout type not supported")
