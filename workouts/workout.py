"""
Workout

Our workout classes
"""


from typing import List


class Workout:
    """
    Workout

    A workout class
    """

    name: str

    def __init__(self, name: str):
        self.name = name


class Lift(Workout):
    """
    Lift

    A lifting type of workout
    """

    weight: int
    reps: List[int]
    sets: List[int]

    def __init__(self, name: str, weight: int, reps: List[int], sets: List[int]):
        super().__init__(name)
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

    distance: int
    time: int
    speed: int
    resistance: int

    def __init__(
        self, name: str, distance: int, time: int, speed: int, resistance: int
    ):
        super().__init__(name)
        self.distance = distance
        self.time = time
        self.speed = speed
        self.resistance = resistance
