"""
Utility functions
"""

from datetime import datetime
import pandas as pd

from workouts.workout import WorkoutFactory, Workout
from workouts.constants import EMPTY_VALS


def parse_cell_into_workout(name: str, date: datetime, cell: str) -> Workout:
    """
    Parse cell data and create the appropriate Workout object
    """
    # sanity check, lowercase it all and remove whitespace
    cell = cell.lower().replace(" ", "")

    # case of no workout data in cell
    if cell in EMPTY_VALS:
        # TODO: What do we return if no data? Will None work in dataframe / graph later?
        return None

    # case of Lift Workout
    # Ex Lift: (20) 20 x 2; (10) 10 x 2
    # if there's an x in it, it's a lift (because reps x sets is required to be a Lift)
    if "x" in cell:
        weights = reps = sets = []
        is_sets = False

        for i, _ in enumerate(cell):
            # (weight)
            if cell[i] == "(":
                # grab digits until )
                weight_str = ""

                while cell[i] != ")":
                    weight_str += cell[i]
                    i += 1

                    # error check - bad data
                    if i > len(cell) - 1:
                        # TODO: handle this error better
                        raise Exception(f"Error parsing cell: {cell}")

                weights.append(int(weight_str))

            # x - toggle between sets and reps
            if cell[i] == "x":
                is_sets = not is_sets

            # sets and reps
            # ; - end of this sets / reps
            digit_str = ""
            while cell[i] != ";" and i < len(cell) - 1:
                digit_str += cell[i]
                i += 1

            if is_sets:
                sets.append(int(digit_str))
            else:
                reps.append(int(digit_str))

        return WorkoutFactory.create_workout(
            "lift", name=name, date=date, weights=weights, reps=reps, sets=sets
        )

    # TODO: case of Cardio Workout
    # Ex Cardio: 20 mins, 10 kmph, 3.0
    return None


def read_csv_input(filepath: str) -> pd.DataFrame:
    """
    Read input from csv into pandas dataframe

    TODO: consider other methods of input
    """
    return pd.read_csv(filepath)
