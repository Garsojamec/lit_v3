import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go # https://plotly.com/python/creating-and-updating-figures/#figures-as-graph-objects

# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
df = pd.read_csv(filepath)

# Step 2.b - Extra Python Code

# Step 3. Create a plotly figure
    # go.Scatter
    ## https://plotly.com/python/line-and-scatter/#scatter-and-line-plot-with-goscatter
    ## https://plotly.com/python/reference/#scatter

    # go.Layout
    ## https://plotly.com/python/creating-and-updating-figures/#the-layout-key
    ## title
    ### https://plotly.com/python/reference/#layout-title
    ## hovermode
    ### https://plotly.com/python/reference/#layout-hovermode

    #go.figure
    ## Beautiful Code structure where things fed into figure are defined separately and modularly

# Step 4. Create a Dash layout ( Overall Layout of Site )
    # app.layout

    # html components
    ## https://dash.plotly.com/dash-html-components

    # html.Div
    ## https://dash.plotly.com/dash-html-components/div

    # dcc - Dash Core Components
    ## https://dash.plotly.com/dash-core-components

    # dcc.Graph - Same syntax as plolty, but feeding arguments via Step 3 is good style
    ## https://dash.plotly.com/dash-core-components


app.layout = html.Div([
                dcc.Graph(id = 'plot_id', figure = fig)
                      ])

# Step 5. Add callback functions


# Step 6. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)
