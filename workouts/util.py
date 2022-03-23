"""
Utility functions
"""

import pandas as pd

from workouts.workout import Workout


def create_workout(data: pd.DataFrame) -> Workout:
    """
    Create a workout from tabular data

    Since I'm in control of what data gets entered, I can assume the schema
    """
    # sample data:
    # Date,Knee Pushups,Full Pushups,Squats,Deadlifts,Curls,Leg Bicycle,Leg Lifts
    # 02/06/2021,Rest,Rest,Rest,Rest,Rest,Rest,Rest
    # 02/07/2021,20 x 2; 15 x 1,0,25 x 3,(25) 20 x 3,(20) 12 x 3,0,0
    # 02/08/2021,20 x 1; 15 x 1; 10 x 1,0,25 x 3,(25) 20 x 3,(20) 15 x 3,0,0

    # TODO: This is temp code
    # get the columns
    schema = data.columns.tolist()

    return schema


def read_csv_input(filepath: str) -> pd.DataFrame:
    """
    Read input from csv into pandas dataframe

    TODO: consider other methods of input
    """
    return pd.read_csv(filepath)
