import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go # https://plotly.com/python/creating-and-updating-figures/#figures-as-graph-objects


# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
filepath="anat_roots.csv"
df = pd.read_csv(filepath)
#print(df.head(4))

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
# trace_1 = go.Scatter(
#     x=df.Date,y=df[" High"],
#     name="Canadian Solar HIGH",
#     line = dict(
#                 width=2,
#                 color="hsl(50,100%,50%)"
#                 )
#         )
#
# layout = go.Layout(
#             title="Canadian Solar High",
#             hovermode="closest"
#                 )
#
# fig = go.Figure(data = [trace_1], layout=layout)
#

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

    # Adding a Header and a Paragraph
    html.Div([
        html.H1("This is first try for vis of Anatomy Roots"),
        html.P("Learning Dash is so interesting!!")
            ],
        style={"padding":"50px",
                "backgroundColor":"hsl(220,100%,65%)"}),
    # # Adding a Plot
    # dcc.Graph(id="plot_id",figure=fig),

    # # From Recipe
    # ## Adding Dropdown from Recipe
    # dcc.Dropdown(
    #     value=['a'],
    #     options=[{'label': i, 'value': i} for i in ['a', 'b', 'c', 'd']],
    #     multi=True,
    #     id='dropdown'
    # ),
    #
    # ## Adding Display of Dropdown Output
    # html.H1(id='output')

    # Dropdown from CSV
    dcc.Dropdown(
        options=[{'label': df.loc[i,:]["Gloss"], 'value':df.loc[i,:]["Phones"]} for i in df.index],
        multi=False,
        id='dropdown_roots',
        placeholder="Select a Gloss",
        value="",
        clearable=False
    ),

    # Displaying Dropdown Value Selected
    html.H1(id='chosen_phone_display')
])

# Step 5. Add callback functions
@app.callback(Output('chosen_phone_display', 'children'), [Input('dropdown_roots', 'value')])
def display_output(value):
    return str(value)


# Step 6. Add the server clause
if __name__ == "__main__":
    app.run_server(debug=True)
