import csv
import json
import requests

api_url = 'http://127.0.0.1:5000/api/endpoint666'
csv_file_path = 'leanspace.title.csv'

def send_api_request(payload):
    print("Payload: ", json.dumps(payload, indent=3) )
    response = requests.post(api_url, json=payload)

    # Check API responses
    if response.status_code == 200:
        print('API request success')
        print(response.json())
    else:
        print('API request fail')
        print(response.status_code, response.text)


def process_csv_file(csv_file, api_url):
    payloads = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            payload = {}
            for column, value in row.items():
                payload[column] = value
            payloads.append(payload)

    # Process each payload with POST request
    for payload in payloads:
        send_api_request(payload)

# Fire this thing up
process_csv_file(csv_file_path, api_url)