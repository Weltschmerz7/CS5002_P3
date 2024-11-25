import pandas as pd
import json as jn

# Pseudo code: This script should automate the data mining process with the following steps
# check the format and validity of variable values
# remove duplicates and deal with missing values
# save the refined dataset as a seperate csv in data subdirectory for subsequent analysis

def clean_data ():
    '''This function checks for consistency and clean the data'''
    data = pd.read_csv('data/Scotland_teaching_file_1PCT.csv')
    # This drops the duplication and fill the missing values with 'Unknown'
    data = data.drop_duplicates().fillna('Unknown')




# def build_input_states():
#     for colunm_type in data_json:
#         #store keys in list
    
#     for row in data:
#         for data_point in row:
#             if data_point not in list
#                 get rid of row 
        # "sasdasd".isnumeric


