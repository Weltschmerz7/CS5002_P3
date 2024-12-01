import pandas as pd
import matplotlib.pyplot as plt;


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
    plt.figure(figsize=(10, 8))  # Adjust figure size

    # Create the pie chart without labels
    wedges, texts, autotexts = plt.pie(
        df_to_plot[values_col],
        autopct='%1.1f%%',           # Show percentage on the chart
        startangle=90,               # Start from the top
        colors=plt.cm.Set3.colors,  # Use a distinct color palette
        textprops={'fontsize': 12},  # Adjust percentage font size
        labeldistance = 1.1,
        pctdistance = 0.85
    )

    # Add a legend next to the chart
    plt.legend(
        wedges,                      # Corresponding wedges (colors)
        df_to_plot[labels_col],            # Labels from the data
        title="Categories",          # Title of the legend
        loc="center left",           # Position it to the left of the chart
        bbox_to_anchor=(1, 0, 0.5, 1),  # Anchor the legend outside the chart
        fontsize=12                  # Legend font size
    )

    plt.title(title, fontsize=16)  # Chart title
    plt.tight_layout()  # Adjust layout to fit everything
    plt.show()
    
    return plt
