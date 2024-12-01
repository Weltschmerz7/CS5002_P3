import ipywidgets as widgets
from ipywidgets import interact
from data_visualization import get_bar, get_pie

# Main interactive plot function
def interactive_plot(data_to_plot, x_col, y_col, char_type = 'bar'):
    '''This function will map the interactive plot function'''

    # Call the appropriate chart function
    if char_type == 'bar':
        get_bar(data_to_plot, x_col, y_col)
    elif char_type == 'pie':
        get_pie(data_to_plot,x_col,y_col)

def get_widge(data_to_plot, x_col = 'x_col', y_col = 'y_col',char_type = 'bar'):
    '''This function gets the widgets for the graphs'''
    # Create widgets
    # Dropdown for chart type selection
    chart_type_widget = widgets.Dropdown(
        options=['bar', 'pie'],
        value=char_type,
        description='Chart Type:'
    )

    # Dropdown for selecting filter column
    filter_column_dropdown = widgets.Dropdown(
        options=[None] + list(data_to_plot.columns),
        value=None,
        description='Filter By:'
    )

    # Dropdown for selecting filter value
    filter_value_dropdown = widgets.Dropdown(
        options=[],
        value=None,
        description='Filter Value:'
    )

    # Update filter values dynamically
    def update_filter_values(*args):
        selected_column = filter_column_dropdown.value
        if selected_column:
            # Update options based on unique values in the selected column
            filter_value_dropdown.options = list(data_to_plot[selected_column].unique())
        else:
            # Reset options if no column is selected
            filter_value_dropdown.options = []

    # Attach observer to update filter values when filter column changes
    filter_column_dropdown.observe(update_filter_values, names='value')

    # Function to filter data and update the plot
    def update_plot(filter_column, filter_value):
        # Apply filtering if both column and value are selected
        data = data_to_plot.copy()
        if filter_column and filter_value:
            data = data[data[filter_column] == filter_value]

    # Interactive widget setup
    interact(
        update_plot,
        chart_type=chart_type_widget,
        filter_column=filter_column_dropdown,
        filter_value=filter_value_dropdown
    )

    # Call the plotting function with the filtered data
    interactive_plot(data_to_plot,x_col, y_col,char_type='bar')