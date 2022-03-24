"""
Tests for Workout classes
"""

import datetime
from unittest import TestCase

from workouts.workout import Workout, Lift, Cardio


class TestWorkout(TestCase):
    """
    Tests for Workout class
    """

    def test_constructor_assigns_members(self):
        """
        Test the constructor assigns all member variables
        """
        name = "Test"
        date = datetime.datetime.now()

        workout = Workout(name=name, date=date)

        self.assertEqual(workout.name, name)
        self.assertEqual(workout.date, date)


class TestLift(TestCase):
    """
    Tests for Workout class
    """

    def test_constructor_assigns_members(self):
        """
        Test the constructor assigns all member variables
        """
        name = "Test"
        date = datetime.datetime.now()
        reps = [20, 10]
        sets = [1, 2]
        weights = [20, 10]

        workout = Lift(name=name, date=date, weights=weights, reps=reps, sets=sets)

        self.assertEqual(workout.name, name)
        self.assertEqual(workout.date, date)
        self.assertEqual(workout.weights, weights)
        self.assertEqual(workout.reps, reps)
        self.assertEqual(workout.sets, sets)

    def test_total_reps_returns_total_reps(self):
        """
        Test the total_reps property returns the total number of reps, accounting for sets and reps
        """
        name = "Test"
        date = datetime.datetime.now()
        reps = [20, 10]
        sets = [1, 2]
        weights = [20, 10]

        workout = Lift(name=name, date=date, weights=weights, reps=reps, sets=sets)

        self.assertEqual(workout.total_reps, 40)

    def test_total_weight_returns_weight_for_all_sets_and_resp(self):
        """
        Test the total_weight property returns the total weight lifted, accounting for sets and reps
        """
        name = "Test"
        date = datetime.datetime.now()
        reps = [20, 10]
        sets = [1, 2]
        weights = [20, 10]

        workout = Lift(name=name, date=date, weights=weights, reps=reps, sets=sets)

        # total weight = (20 * 1 * 20) + (10 * 2 * 10) = 600
        self.assertEqual(workout.total_weight, 600)


class TestCardio(TestCase):
    """
    Tests for Workout class
    """

    def setUp(self):
        """
        Create a default Cardio workout
        """
        name = "Test"
        date = datetime.datetime.now()
        times = [20, 15, 120]
        time_units = ["m", "m", "s"]
        speeds = [10, 5, 1]
        speed_units = ["km/h", "mi/h", "m/s"]
        resistances = [1, 2, 3]
        distances = [5, 3, 500]
        distance_units = ["km", "mi", "m"]

        self.workout = Cardio(
            name=name,
            date=date,
            times=times,
            time_units=time_units,
            speeds=speeds,
            speed_units=speed_units,
            resistances=resistances,
            distances=distances,
            distance_units=distance_units,
        )

    def test_constructor_assigns_members(self):
        """
        Test the constructor assigns all member variables
        """
        name = "Test"
        date = datetime.datetime.now()
        times = [20, 15, 120]
        time_units = ["m", "m", "s"]
        speeds = [10, 5, 1]
        speed_units = ["km/h", "mi/h", "m/s"]
        resistances = [1, 2, 3]
        distances = [5, 3, 500]
        distance_units = ["km", "mi", "m"]

        workout = Cardio(
            name=name,
            date=date,
            times=times,
            time_units=time_units,
            speeds=speeds,
            speed_units=speed_units,
            resistances=resistances,
            distances=distances,
            distance_units=distance_units,
        )

        self.assertEqual(workout.name, name)
        self.assertEqual(workout.date, date)
        self.assertEqual(workout.times, times)
        self.assertEqual(workout.time_units, time_units)
        self.assertEqual(workout.speeds, speeds)
        self.assertEqual(workout.speed_units, speed_units)
        self.assertEqual(workout.resistances, resistances)
        self.assertEqual(workout.distances, distances)
        self.assertEqual(workout.distance_units, distance_units)

    def test_get_distance_units_from_speed_units(self):
        """
        Test the get_distance_units method returns the distance units from the speed units
        """
        self.workout.speed_units = ["m/s", "ft/s", "km/h", "mi/h", "yd/m"]
        expected_result = ["m", "ft", "km", "mi", "yd"]

        result = self.workout._get_distance_units_from_speed_units()

        self.assertEqual(result, expected_result)

    def test_get_distances_from_speed_and_time(self):
        """
        Test the get_distances method returns the distances, accounting for units
        """
        # TODO: This will change when the conversion function is implemented
        self.workout.distances = []
        self.workout.times = [20, 15, 120]
        self.workout.time_units = ["m", "m", "s"]
        self.workout.speeds = [10, 5, 1]
        self.workout.speed_units = ["km/h", "mi/h", "m/s"]
        expected_result = [200, 75, 120]

        result = self.workout._get_distances_from_speed_and_time()

        self.assertEqual(result, expected_result)
