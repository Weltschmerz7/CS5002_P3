import matplotlib.pyplot as plt;
import pandas as pd



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
    
def get_bar (data_to_plot, x_col, y_col, title = 'Bar chart', xlabel = 'X-axis', ylabel = 'Y-axis'):
    '''This function takes in the data to plot, and make the bar chart '''
    
    plt.figure(figsize=(12, 8))

    plt.barh(data_to_plot[x_col], data_to_plot[y_col], color='skyblue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.xticks(rotation=60)
    plt.title(title)
    plt.tight_layout()
    plt.show()
    return plt

def get_pie (df_to_plot, labels_col, values_col, title = 'Pie chart'):
    '''This function takes in the data to plot, and make the pie chart'''
    plt.figure(figsize=(10, 8)) # Adjust figure size

    # Create the pie chart (only wedges and labels are returned)
    wedges, texts = plt.pie(
        df_to_plot[values_col],
        startangle=90,
        colors=plt.cm.Set3.colors,
    )

    # Get the legend labels with percentages
    legend_labels = [
        f"{category} ({percentage:.1f}%)"
        for category, percentage in zip(df_to_plot[labels_col], df_to_plot[values_col])
    ]

    # Add a legend with percentages
    plt.legend(
        wedges,                      # Wedges (colors)
        legend_labels,               # Labels with percentages
        title="Categories",          
        loc="center left",           
        bbox_to_anchor=(1, 0, 0.5, 1),  # Place legend outside the chart
        fontsize=12                  
    )

    # Add the title
    plt.title(title, fontsize=16)

    # Adjust layout to fit everything
    plt.tight_layout()
    plt.show()



