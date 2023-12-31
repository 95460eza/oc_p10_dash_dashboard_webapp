
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc  # To define rows and columns on the page
import dash_mantine_components as dmc  # To define a grid on the page within which to insert dmc.Cols and define their width by assigning a number to the span property.
import pandas as pd
import plotly.express as px
import os


# Creates the DASH INTERACTIVE web app OBJECT (content is interactive and will be seen in an browser)
# Incorporate styling Dash Bootstrap Components
# external_stylesheets = [dbc.themes.CERULEAN]
# OR
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
# app6 = Dash(__name__, external_stylesheets=external_stylesheets)
app6 = Dash(__name__)




# Define the Web App Layout
app6.layout = html.Div([

                        # The html.Div() (note the ABSENCE of []) DASH COMPONENT with children= parameter adds TEXT to the webpage
                        html.Div(children='Welcome DATA Apprentice')

                        ])

#if __name__ == '__main__':
#    app6.run(debug=True)
#   app6.run(host='0.0.0.0', port=5000, debug=True)
