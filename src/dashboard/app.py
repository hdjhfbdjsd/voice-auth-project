# src/dashboard/app.py
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
server = app.server  # for deployment if needed

app.layout = html.Div([
    html.H2("Voice Auth Dashboard (MVP)"),
    html.P("Use the API to upload audio and view results here."),
    html.Div(id="status", children="Ready")
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
