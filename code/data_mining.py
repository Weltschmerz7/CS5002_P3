#!/usr/bin/env python3 
import pandas as pd
import json as jn

def map_data (data_to_map, json_map):
    '''This helper function maps the coded csv to decoded csv using json file'''
    decode_helper = json_map
    for column in data_to_map.columns:
        if column in decode_helper:
            data_to_map[column] = data_to_map[column].map(decode_helper[column])
    print(f'csv data with {len(data_to_map)} records decoded! ')
    return data_to_map
    
# Pseudo code: This script should automate the data mining process with the following steps
# check the format and validity of variable values
# remove duplicates and deal with missing values
# save the refined dataset as a seperate csv in data subdirectory for subsequent analysis

def clean_data (csv = './data/Scotland_teaching_file_1PCT.CSV'):
    '''This function checks for consistency and clean the data'''
    # hardcode the file in because this is the assigned file to read
    data = pd.read_csv(csv, dtype=str)
    # load the json file
    with open('data/data_dictionary.json', 'r') as f:
        # the valid_rules is a dictionary of dictionaries. 
        valid_rules = jn.load(f)
    # make the original_columns to a list to compare with the potentially modified columns
    original_columns = data.columns.to_list()

    # turn the column names in csv and json file to lower case to help with consistency
    valid_rules = {k.lower(): v for k, v in valid_rules.items()}
    data.columns = data.columns.str.strip().str.lower()
    # check and drop duplication
    duplicates = data[data.duplicated()]
    if not duplicates.empty:
        print(f'Duplication of {len(duplicates)} records found, dropping duplication and saving a seperate cleaned csv file..')
    data = data.drop_duplicates()
    # drop the missing values
    data = data.dropna()
    # check and drop missing value
    nan_count = data.columns.isnull().sum()
    if nan_count > 0:
        print(f'column "{column}" has {nan_count} missing data, filling column with missing data')
        #  fill the missing values with a place holder
        data.columns = data.columns.fillna('NaN')
    
    # initialize an empty dataframe to store all invalid rows that don't match the json rules
    invalid_rows = pd.DataFrame(columns = data.columns)
    
    for column in data.columns:
        if column in valid_rules:
            # put all the keys that the specific column header have in a set
            valid_set = {str(i) for i in valid_rules[column].keys()}
            # outline the invalide rows that contain code which does not belong to the valid_set
            # use the ~ bitwise NOT operator to collect the invalid rows
            invalid_mask = ~data[column].isin(valid_set)
            # get the actual invalid rows
            invalid_row = data[invalid_mask]
            # add each invalid row into invalid rows dataframe
            invalid_rows = pd.concat([invalid_rows, invalid_row], ignore_index=True)
            # drop all the invalid columns
            data = data[~invalid_mask]
    # this is where i can call the function to map the csv, because at this point data is cleaned
    # call the helper functin to map everything to the cleaned data
    mapped_data = map_data(data,valid_rules)

    # only create extra files if the data needs cleaning
    if len(invalid_rows) != 0 or len(duplicates) != 0 or nan_count > 0:
        mapped_data.to_csv('data/cleaned_data.csv', index=False)
        invalid_rows.to_csv('data/invalid_data.csv', index=False)
        print(f'Data cleaned, stored {len(invalid_rows)} records of invalid data in a seperate csv file. Cleaned data is ready to be processed!')
    elif original_columns != list(mapped_data.columns):
        mapped_data.to_csv('data/cleaned_data.csv', index=False)
        print('Data columns have been cleaned and new csv file is saved in the data directory!')
    else:
        print('the raw data is clean and no further processing needed!')

    return mapped_data, invalid_rows
 
clean_data()

