import pandas as pd
import matplotlib.pyplot as plt


def dict_to_df (dict_to_trans, col_names = None):
    '''Tihs helper function turns dictionary to df, for readability and consistency'''
    if isinstance(next(iter(dict_to_trans.keys())), tuple):
        # handle the transformation if the keys are tuple
        df = pd.DataFrame.from_dict(dict_to_trans, orient='index', columns=[col_names[-1]])
        df.reset_index(inplace=True)
        # split the tuple keys to two and transform to dataframe
        df[col_names[:-1]] = pd.DataFrame(df['index'].tolist(), index=df.index)
        # drop the index from the df and overwrite df
        df.drop(columns='index', inplace=True)
        return df[col_names]
    
    elif isinstance(next(iter(dict_to_trans.values())), dict):
        # also handle nested dictionary
        rows = []
        # looping through the keys and values of nested dictionary
        for first_key, first_dict in dict_to_trans.items():
            for second_key, value in first_dict.items():
                # separate the nested dictionaries
                rows.append([first_key,second_key,value])
        return pd.DataFrame(rows,columns=col_names)
    
    else:
        # if the dictionary just have simple key value pair, transform them
        df = pd.DataFrame.from_dict(dict_to_trans, orient='index', columns=[col_names[1]])
        # reset the index while overwriting the df
        df.reset_index(inplace=True)
        df.columns = col_names
        return df
    
# def get_bar (data_to_plot):
#     '''This function takes in the data to plot, and make the bar chart '''


# def get_pie (data_to_plot):
#     '''This function takes in the data to plot, and make the pie chart'''

