import pandas as pd
import json as jn
import numpy as np

# read the csv
teaching_data = pd.read_csv('data/Scotland_teaching_file_1PCT.csv')

# get the labels to distinguish between numerical sumbols 
with open ('data/data_dictionary.json', 'r') as f:
    labels = jn.load(f)

