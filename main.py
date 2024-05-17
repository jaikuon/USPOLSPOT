#US Political Hotspot Map by jaikuon
#This program is designed to visualize US county data
#to specifically show how counties vary in political leaning
#May add way to calculate other demographic factors such as income, race, and population.

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][0]
print(counties)