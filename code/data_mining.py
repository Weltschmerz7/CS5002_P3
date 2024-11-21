import pandas as pd
import json as jn


def map_data ():
    '''This function maps the numeric data in the csv file and gives the context provided in the JSON file'''
    # Read the csv file in the data folder
    csv_data = pd.read_csv('data/Scotland_teaching_file_1PCT.csv', 'r')
    csv_data = csv_data.drop_duplicates()

    # load the data from the data_dictionary.json file
    with open ('data/data_dictionary.json', 'r') as f:
        map = jn.load(f)
    
    # apply the logic to map the context to each encoded number
    for col, col_map in map.items():
        # check if the column exist in the csv data's colum
        if col in csv_data.columns:
            csv_data[col] = csv_data[col].map(col_map).fillna('Unknown')

    # save the mapped data in another csv file
    csv_data.to_csv('cleaned_data.csv', index = False)

    return csv_data

    



    




