import pandas as pd



def dict_to_df (dict, col_names = None):
    '''Tihs helper function turns dictionary to df, for readability and consistency'''
    if isinstance(next(iter(dict.keys())), tuple):
        # handle the transformation if the keys are tuple
        df = pd.DataFrame.from_dict(dict, orient='index', columns=[col_names[-1]])
        df.reset_index(inplace=True)
        df[col_names[:-1]] = pd.DataFrame(df['index'].tolist(), index=df.index)
        df.drop(columns='index', inplace=True)
        return df[col_names]
    else:
        # if the dictionary just have simple key value pair, transform them
        df = pd.DataFrame.from_dict(dict, orient='index', columns=[col_names[1]])
        df.reset_index(inplace=True)
        df.columns = col_names
        return df
# def get_bar (data_to_plot):
#     '''This function takes in the data to plot, and make the bar chart '''


# def get_pie (data_to_plot):
#     '''This function takes in the data to plot, and make the pie chart'''

