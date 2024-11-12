# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:09:36 2024
"""

import os
import numpy as np
import pandas as pd

# Definition of the file name
file_name = "results_experiment.csv"

if os.path.isfile(file_name):
    # If the file exists, it opens the file and read it
    df_results = pd.read_csv(file_name)
else:
    # If it doesn't, it creates a .csv file with the name 'results_experiment.csv'
    df_results = pd.DataFrame(columns=["participant_ID", "vis_type", "correct_answer", "time_(s)"])  # Creation of a dataframe

# Function to get id and create a new one
def get_id(df): return 0 if df.empty else (df.iloc[-1, 0] + 1)

def add_result(df, part_id, v_type, answer, t):
    # Create a new row as a DataFrame
    result = pd.DataFrame([[part_id, v_type, answer, t]], columns=df.columns)
    return pd.concat([df, result], ignore_index=True)
  
# Add the new result and update the dataframe
df_results = add_result(df_results)

df_results.to_csv("results_experiment.csv", index=False)