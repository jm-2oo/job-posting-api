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

response = gmaps.places(
    query="hotels",
    location=(51.491329, -0.195332),
    radius=50000 #km
)

#extract and store place_id
place_id_list = []

#get the place_id only
for result in response['results']:
    place_id_list.append(result['place_id'])
    
#store below output 
place_data = []

for pid in place_id_list:
    details = gmaps.place(place_id=pid)
    result = details.get('result', {})
    place_data.append({
        'Name': result.get('name'),
        'Website': result.get('website'),
        'Address': result.get('formatted_address')
    })

#store as a df
df = pd.DataFrame(place_data)

#export to csv
df.to_csv('maps.csv', index='False')
print('Saved as: maps.csv')