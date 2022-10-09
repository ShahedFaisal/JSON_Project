import json

infile = open('US_fires_9_1.json','r')

fires = json.load(infile)

brights = [fires[index]['brightness'] for index,item in enumerate(fires) if fires[index]['brightness'] > 450]
lats = [fires[index]['latitude'] for index,item in enumerate(fires) if fires[index]['brightness'] > 450]
lons = [fires[index]['longitude'] for index,item in enumerate(fires) if fires[index]['brightness'] > 450]

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = {'type':'scattergeo',
        'lon':lons,
        'lat':lats,
        'marker':{
            'size':[15*b/b for b in brights],
            'color':brights,
            'colorscale':'Viridis',
            'reversescale':True,
            'colorbar':{'title':'Brightness'}
        }}

layout = Layout(title='US Fires - 9/1/2020 through 9/13/2020')
fig = {'data':data, 'layout':layout}
offline.plot(fig, filename='US_fires_9_1.html')