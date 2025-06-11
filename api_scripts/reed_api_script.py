from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd
import csv
from pathlib import Path

#define path to secrets
secrets_path = Path('reed_api/secrets/config.json')

#get secrets
with open(secrets_path, "r") as f:
    secrets = json.load(f)

#use secret
api_key = secrets['API_KEY']
password = secrets['PASSWORD']

keyword = 'data analyst'
location = 'UK'
distance = 5
direct_employer = 'true'
limit_results = ''

url = f'https://www.reed.co.uk/api/1.0/search?keywords={keyword}&locationName={location}&distanceFromLocation={distance}&postedByDirectEmployer={direct_employer}&resultsToTake={limit_results}'

#get posting api data and parse as json
response = requests.get(url, auth = HTTPBasicAuth(api_key, password))
result = response.json()

#convert to list
result = list(result.values())

#get only the first items from the list
data = result[0]

#flatten json and conver to df
flatten_json = pd.json_normalize(data)
df = pd.DataFrame(flatten_json)

#write to CSV
df.to_csv('reed.csv', index='False')
print('Saved as: reed.csv')