import folium
import pandas 

waterfalls = pandas.read_csv('waterfall.txt')
lat = list(waterfalls['Latitude'])
lon = list(waterfalls['Longitude'])
name = list(waterfalls['Name'])
height = list(waterfalls['Height'])
state = list(waterfalls['State'])

map = folium.Map(location=[32,53],zoom_start = 5)

# waterfalls
fg_w = folium.FeatureGroup("WaterFalls")
# country borders
fg_b = folium.FeatureGroup(name ="Countries Borders")


# borders
# we can use Path instead open()
world_data = open('world.json',encoding='utf-8-sig').read()
folium.GeoJson(data=world_data).add_to(fg_b)

# waterfalls
def color_producer(height):
    if height<20:
        return 'green'
    elif height<50 :
        return 'red'   
    else:
        return 'black'    

for lt,ln,nm,hg,st in zip(lat,lon,name,height,state):
    html = f"""
        <h5>Name:{nm}</h5>
        <h5>Height:{hg} meters</h5>
        <h5>State:{st}</h5>
        <a href='https://google.com/search?q={nm} waterfall'>Read More : </a>
        <br>
        <span>(Open in new tab)</span>
    """
    fg_w.add_child(folium.CircleMarker(location=[lt,ln],popup = html,radius = 10,fill_color=color_producer(hg),color='black'))



map.add_child(fg_w)
map.add_child(fg_b)

# layer control
map.add_child(folium.LayerControl())

map.save("map.html") 