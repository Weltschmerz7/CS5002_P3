import pandas as pd
import json as jn

def map_data (df_to_map):
    '''This function maps the numeric data in the csv file and gives the context provided in the JSON file'''
    # Load the structure from json file to map 
    with open ('data/data_dictionary.json', 'r') as f:
        map = jn.loads(f)
    
    # apply the logic to map the context to each encoded number
    for col, col_map in map.items():
        # check if the column exist in the csv data's colum
        if col in df_to_map.columns:
            df_to_map[col] = df_to_map[col].map(col_map).fillna('Unknown')

    return df_to_map

