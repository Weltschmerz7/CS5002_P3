#!/usr/bin/env python3 
import pandas as pd
import json as jn

def map_data (data_to_map, dict_name, map_file ='data/data_dictionary.json', place_holder = 'Unknown'):
    '''This function recursively maps the numeric data in the csv file and gives the context provided in the json file'''
    # Load the structure from json file to map 
    with open (map_file, 'r') as f:
        map = jn.load(f)

    # get the specific dictionary to map
    target_dict = data_to_map.get(dict_name, {})

    # perform the mapping
    mapped_data = {}
    if isinstance(target_dict,dict):
        for key, value in target_dict.items():
            if isinstance (value,dict):
                mapped_data[key] = {map.get(str(k_inner),place_holder): v_inner for k_inner, v_inner in value.items()}
            else:
                mapped_data[map.get(str(key),place_holder)] = value
        # update the original dictionary to the mapped dictionary
        data_to_map[dict_name] = mapped_data
        return data_to_map
             

def analyze_csv (csv_data):
    '''This function performs all the neccessary statistical analysis of the csv dataset and store them in a dictionary'''
    # load the csv data
    with open(csv_data, 'r') as f:
        data = pd.read_csv(f)
    
    results = {}
    # Requirement 1: get the total number of records in the dataset
    results['total_record'] = len(data)
    # Requirement 2: get the type of each variable in the dataset
    results['data_types'] = data.dtypes.to_dict()
    # Requirement 3: summary list of all different values that each column takes and the frequencies. except 'record_number' and 'region'
    excluded_columns = ['record_number', 'region']
    value_count = {}
    for column in data.columns:
        if column not in excluded_columns:
            value_count[column] = data[column].value_counts().to_dict()
    results['value_counts'] = value_count
    # Requirement 4: get the number of records for each age group
    results['age_count'] = data['age'].value_counts().to_dict()
    # Requirement 5: get the number of records for each occupation
    results['occupation_counts'] = data['occupation'].value_counts().to_dict()
    # Requirement 6: get the percentage of records for each general health descripter
    health_counts = data['health'].value_counts(normalize=True) * 100
    results['health_percentages'] = health_counts.round(2).to_dict()
    # Requirement 7: get the percentage of records of each ethnic group
    ethnic_group_counts = data['ethnic_group'].value_counts(normalize=True) * 100
    results['ethnic_group_percentages'] = ethnic_group_counts.round(2).to_dict()
    # Requirement 8: get the number of records by hours worked per week and industry
    results['hours_worked_by_industry'] = (data.groupby(['hours_worked_per_week', 'industry']).size().to_dict())
    # Requirement 9: get the number of records by occupation and approximate social grade
    results['occupation_by_social_grade'] = (data.groupby(['occupation', 'approximate_social_grade']).size().to_dict())
    # Requirement 10: get the number of economically active people depending on age
    active_codes = ['1', '2', '3', '4']  # economically active codes
    results['economically_active_by_age'] = (data.loc[data['economic_activity'].isin(active_codes)].groupby('age').size().to_dict())
    # Requirement 11: get the number of economically inactive people depending on a health descriptor
    inactive_codes = ['5', '6', '7', '8', '9']  # economically inactive codes
    results['economically_inactive_by_health'] = (data.loc[data['economic_activity'].isin(inactive_codes)].groupby('health').size().to_dict())
    # Requirement 12: get the number of working hours per week for students
    student_codes = ['4', '6']  # full-time and part-time student codes
    results['working_hours_for_students'] = (data.loc[data['economic_activity'].isin(student_codes)].groupby('hours_worked_per_week').size().to_dict())
    # print(f'one of the result dictionary! : {results["age_count"]}')
    print(results)
    return results

# make the script executable 
if __name__ == '__main__':
        analyze_csv('data/cleaned_data.csv')