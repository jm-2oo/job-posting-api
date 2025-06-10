##useful code for future reference##

from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd
import csv
from pathlib import Path

#define path to secrets
secrets_path = Path("secrets/config.json")

#get secrets
with open(secrets_path, "r") as f:
    secrets = json.load(f)

#use secret
api_key = secrets["API_KEY"]
password = 'blank'

keyword = 'data analyst'
location = 'united kingdom'
distance = 5
direct_employer = ''
limit_results = '3'

url = f'https://www.reed.co.uk/api/1.0/search?keywords={keyword}&locationName={location}&distanceFromLocation={distance}&postedByDirectEmployer={direct_employer}&resultsToTake={limit_results}'

#get posting api data and parse as json
response = requests.get(url, auth = HTTPBasicAuth(api_key, password))
result = response.json()

##check if it's a list or dictionary##
if isinstance(result, dict):
    print("It's a dictionary.")
elif isinstance(result, list):
    print("It's a list.")
else:
    print("It's something else.")