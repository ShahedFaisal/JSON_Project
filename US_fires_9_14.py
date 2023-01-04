import json

#Open and load JSON file
infile = open('US_fires_9_14.json','r')
fires = json.load(infile)


#Get brighness, longitude and lattitude of fires using list comprehension
brights = [fires[index]['brightness'] for index,item in enumerate(fires) if fires[index]['brightness'] > 450]
lons = [fires[index]['longitude'] for index,item in enumerate(fires) if fires[index]['brightness'] > 450]
lats = [fires[index]['latitude'] for index,item in enumerate(fires) if fires[index]['brightness'] > 450]


#Create offline geoplot to visualize fires
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = {
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[15*b/b for b in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}
mylayout = Layout(title='US Fires: 9/14/2020 through 9/20/2020')
fig = {'data':data, 'layout':mylayout}
offline.plot(fig, filename='US_fires_9_14.html')