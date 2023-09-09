import json

# Open and load JSON file
infile = open('eq_30_days_data.json','r')
eqdata = json.load(infile)


# Convert JSON file to readable dictionary format
readablefile = open('eq_30_days_data_readable.json','w')
json.dump(eqdata,readablefile,indent=4)
readablefile.close()


# Get magnitude, longitude, lattitude and place of  earthquakes using list comprehension
mags = [eq['properties']['mag'] for eq in eqdata['features']]
lons = [eq['geometry']['coordinates'][0] for eq in eqdata['features']]
lats = [eq['geometry']['coordinates'][1] for eq in eqdata['features']]
places = [eq['properties']['place'] for eq in eqdata['features']]


# Create offline geoplot to visualize earthquakes
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = {
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':places,
    'marker':{
        'size':[5*m for m in mags],
        'color':mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Magnitude'}
    }
}
mylayout = Layout(title='Global Earthquakes (30 days)')
fig = {'data':data, 'layout':mylayout}
offline.plot(fig, filename='eq_30_days_plot.html')