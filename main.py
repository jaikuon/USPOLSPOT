#US Political Hotspot Map by jaikuon
#This program is designed to visualize US county data
#to specifically show how counties vary in political leaning
#May add way to calculate other demographic factors such as income, race, and population.

from urllib.request import urlopen
import json
import pandas as pd
import csv
import plotly.express as px


result = pd.read_csv("election.csv")

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("election.csv", dtype={"county_fips": str})



fig = px.choropleth(df, geojson=counties, locations='county_fips', color='per_point_diff',
                           color_continuous_scale="bluered",
                           range_color=(-1, 1),
                           scope="usa",
                           labels={'per_point_diff':'Per Point Difference'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()