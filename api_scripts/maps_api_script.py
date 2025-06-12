import requests
from pathlib import Path
import json 
import googlemaps
import time
import pandas as pd
import time

#secret stuff
secrets_path = Path('secrets/config.json')

with open(secrets_path, 'r') as f:
    secrets = json.load(f)

api_key = secrets['maps_api_key']
gmaps = googlemaps.Client(api_key) 

#params for place to search
response = gmaps.places(
    query="art gallery",
    location=(51.496617, -0.176251),
    radius=50000 #km
)

#extract and store place_id
place_id_list = []

#get list of place_ids
for result in response['results']:
    place_id_result = result['place_id'] #get place_ids and put in place_id_result with result()
    place_id_list.append(place_id_result) #append place_ids to empty list

#with place_ids, get the place detail and store in list
place_data = [] #declare empty list

for pid in place_id_list:
    details = gmaps.place(place_id=pid) #iterate through place_ids to get place details
    result = details.get('result', {})  #get 'result' from places, return {} if not found
    place_details = {                      #extract the name, website and address (JSON markup)
        'Name': result.get('name'),
        'Website': result.get('website'),
        'Address': result.get('formatted_address')
    }
    
place_data.append(place_details) #append to place_data

#store as a df
df = pd.DataFrame(place_data)

#export to csv
version = 'art'
df.to_csv('output_data/maps_' + version + '.csv', index='False')
print('Saved as:' + 'maps_' + version + '.csv')