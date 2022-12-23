import json

infile = open('eq_data_30_day_m1.json','r')

jsonfile = open('readable_eq_data.json','w')
eqdata = json.load(infile)
json.dump(eqdata,jsonfile,indent=4)

list_of_eq = eqdata['features']

mags = []
lons = []
lats = []
places = []

for eq in list_of_eq:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    place = eq['properties']['place']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    places.append(place)

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = {'type':'scattergeo',
        'lon':lons,
        'lat':lats,
        'text':places,
        'marker':{
            'size':[5*m for m in mags],
            'color':mags,
            'colorscale':'Viridis',
            'reversescale':True,
            'colorbar':{'title':'Magnitude'}
        }}

mylayout = Layout(title='Global Earthquakes (30 days)')
fig = {'data':data, 'layout':mylayout}
offline.plot(fig, filename='global_eqs_30_day.html')