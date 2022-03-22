"""
Workout

Our workout classes
"""


import datetime
from typing import List


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

    weight: int
    reps: List[int]
    sets: List[int]

    def __init__(
        self, name: str, date: datetime, weight: int, reps: List[int], sets: List[int]
    ):
        super().__init__(name, date)
        self.weight = weight
        self.reps = reps
        self.sets = sets

    @property
    def total_reps(self) -> int:
        """
        Returns the total number of reps for this lift
        """
        total_reps = 0
        for rep, idx in enumerate(self.reps):
            total_reps += self.sets[idx] * rep
        return total_reps


class Cardio(Workout):
    """
    Cardio

    A cardio type of workout
    """

    # TODO: time and speed need to account for units
    time: int
    speed: int
    resistance: int

    def __init__(
        self,
        name: str,
        date: datetime,
        time: int,
        speed: int,
        resistance: int,
    ):
        super().__init__(name, date)
        self.time = time
        self.speed = speed
        self.resistance = resistance

    @property
    def distance(self) -> int:
        """
        Returns the distance of this cardio workout
        """
        return self.time * self.speed


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
