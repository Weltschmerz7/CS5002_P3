#!/usr/bin/env python3 
import pandas as pd
import json as jn


# Pseudo code: This script should automate the data mining process with the following steps
# check the format and validity of variable values
# remove duplicates and deal with missing values
# save the refined dataset as a seperate csv in data subdirectory for subsequent analysis

def clean_data ():
    '''This function checks for consistency and clean the data'''
    # hardcode the file in because this is the assigned file to read
    data = pd.read_csv('data/Scotland_teaching_file_1PCT.csv')

    # load the json file
    with open('data/data_dictionary.json', 'r') as f:
        # the valid_rules is a dictionary of dictionaries.
        # the key for the outer dictionary is each column header
        # the key for inner dictionary is each code 
        valid_rules = jn.load(f)
    # check if there are any duplications, if there is, drop them and put cleaned csv in seperate file
    duplicates = data[data.duplicated()]
    if not duplicates.empty:
        print(f'Duplication of {len(duplicates)} records found, dropping duplication and saving a seperate cleaned csv file..')
        data = data.drop_duplicates().fillna('NaN')
    # initialize an empty dataframe to store all invalid rows that don't match the json rules
    invalid_rows = pd.DataFrame(columns = data.columns)
    for column in data.columns:
        if column in valid_rules:
            # convert all series into string to aid comparison, in this context, it does not matter if the csv codes are string numbers
            data[column] = data[column].astype(str)
            # put all the keys that the specific column header have in a set
            valid_set = {str(i) for i in valid_rules[column].keys()}
            # outline the invalide rows that contain code which does not belong to the valid_set
            # use the ~ bitwise NOT operator to collect the invalid rows
            invalid_mask = ~data[column].isin(valid_set)
            # get the actual invalid rows
            invalid_row = data[invalid_mask]
            # add each invalid row into invalid rows dataframe
            invalid_rows = pd.concat([invalid_rows, invalid_row], ignore_index=True)
            # use ~ to select all the rows that computed the 'True' boolean
            data = data[~invalid_mask]

    # only create extra files if the data needs cleaning
    if len(invalid_rows) != 0 or len(duplicates) != 0:
        data.to_csv('data/cleaned_data.csv', index=False)
        invalid_rows.to_csv('data/invalid_data.csv', index=False)
        print(f'Data cleaned, stored {len(invalid_rows)} records of invalid data in a seperate csv file. Cleaned data is ready to be processed!')
    else:
        print('the raw data is clean and no further processing needed!')

# make the script executable and provide correct usage if wrong arguments were used
if __name__ == '__main__':
        clean_data()








