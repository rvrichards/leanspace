import csv
import json
import requests

def send_api_request(url, payload):
    print("Payload: ", json.dumps(payload, indent=3) )
    response = requests.post(url, json=payload)
    # Handle the API response here
    print("Response (" , response.status_code, ") ",  response.json())
    

def process_csv_file(csv_file, api_url):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            send_api_request(api_url, row)

# csv file and local api endpoint
csv_file_path = 'leanspace.csv'
api_url = 'http://127.0.0.1:5000/api/endpoint666'

process_csv_file(csv_file_path, api_url)