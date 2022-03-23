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

    def test_constructor_assigns_members(self):
        """
        Test the constructor assigns all member variables
        """
        name = "Test"
        date = datetime.datetime.now()
        time = 20
        speed = 10
        resistance = 3
        workout = Cardio(
            name=name, date=date, time=time, speed=speed, resistance=resistance
        )
        self.assertEqual(workout.name, name)
        self.assertEqual(workout.date, date)
        self.assertEqual(workout.time, time)
        self.assertEqual(workout.speed, speed)
        self.assertEqual(workout.resistance, resistance)

    def test_distance_equals_speed_multiplied_by_time(self):
        """
        Test the distance property returns the distance, accounting for units
        """
        name = "Test"
        date = datetime.datetime.now()
        time = 20
        speed = 10
        resistance = 3
        workout = Cardio(
            name=name, date=date, time=time, speed=speed, resistance=resistance
        )
        self.assertEqual(workout.distance, 200)
