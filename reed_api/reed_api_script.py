from requests.auth import HTTPBasicAuth
import requests
import json
import pandas as pd
import csv
from pathlib import Path

# Define path to your secrets file
secrets_path = Path('reed_api/secrets/config.json')

# Load secrets
with open(secrets_path, "r") as f:
    secrets = json.load(f)

# Use your secret
api_key = secrets["API_KEY"]
password = 'blank'

keyword = 'data analyst'
location = 'UK'
distance = 5
direct_employer = 'true'
limit_results = ''

url = f'https://www.reed.co.uk/api/1.0/search?keywords={keyword}&locationName={location}&distanceFromLocation={distance}&postedByDirectEmployer={direct_employer}&resultsToTake={limit_results}'

#get posting api data and parse as json
response = requests.get(url, auth = HTTPBasicAuth(api_key, password))
result = response.json()

#convert to list so can export to csv
data = list(result.values())

#get only the first item in the list 
job_list = data[0]

#write to CSV
with open('reed.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=job_list[0].keys())
    writer.writeheader()
    writer.writerows(job_list)

print("CSV saved: reed.csv")