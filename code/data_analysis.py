import pandas as pd
import json as jn

def map_data (data_to_map):
    '''This function maps the numeric data in the csv file and gives the context provided in the JSON file'''
    # Load the structure from json file to map 
    with open ('data/data_dictionary.json', 'r') as f:
        map = jn.loads(f)
    # apply the logic to map the context to each encoded number
    for col, col_map in map.items():
        # check if the column exist in the csv data's colum
        if col in data_to_map.columns:
            data_to_map[col] = data_to_map[col].map(col_map).fillna('Unknown')
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
    # Requirement 3: summary list of all different values that each column takes and the frequencies. Except 'Record_Number' and 'Region'
    excluded_columns = ['Record_Number', 'Region']
    value_count = {}
    for column in data.columns:
        if column not in excluded_columns:
            value_count[column] = data[column].value_counts().to_dict()
    results['value_counts'] = value_count
    # Requirement 4: get the number of records for each age group, output a list
    results['age_count'] = data['age'].value_counts().to_dict()
    # Requirement 5: get the number of records for each occupation
    results["occupation_counts"] = data["Occupation"].value_counts().to_dict()
    # Requirement 6: get the percentage of records for each general health descripter
    health_counts = data["health"].value_counts(normalize=True) * 100
    results["health_percentages"] = health_counts.to_dict()
    # Requirement 7: get the percentage of records of each ethnic group
    ethnic_group_counts = data["Ethnic_Group"].value_counts(normalize=True) * 100
    results["ethnic_group_percentages"] = ethnic_group_counts.to_dict()
    # Requirement 8: get the number of records by hours worked per week and industry
    results["hours_worked_by_industry"] = (
            data.groupby(["Hours_Worked_Per_Week", "industry"]).size().to_dict()
        )
    # Requirement 9: get the number of records by occupation and approximate social grade
    results["occupation_by_social_grade"] = (
            data.groupby(["Occupation", "Approximate_Social_Grade"]).size().to_dict()
        )
    # Requirement 10: get the number of economically active people depending on age
    active_codes = ["1", "2", "3", "4"]  # Economically active codes
    active_data = data[data["Economic_Activity"].isin(active_codes)]
    results["economically_active_by_age"] = active_data["age"].value_counts().to_dict()
    # Requirement 11: get the number of economically inactive people depending on a health descriptor
    inactive_codes = ["5", "6", "7", "8", "9"]  # Economically inactive codes
    inactive_data = data[data["Economic_Activity"].isin(inactive_codes)]
    results["economically_inactive_by_health"] = inactive_data["health"].value_counts().to_dict()
    # Requirement 12: get the number of working hours per week for students
    student_codes = ["4", "6"]  # Full-time and part-time student codes
    student_data = data[data["Economic_Activity"].isin(student_codes)]
    results["working_hours_for_students"] = student_data["Hours_Worked_Per_Week"].value_counts().to_dict()

    return results
