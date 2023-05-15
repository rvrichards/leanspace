import csv
import sys
import json
import requests

api_key = 'JamesBond007'  # This is a valid key
api_not = 'NotAValidKey'  # This is a NOT a valid key
api_url = 'http://127.0.0.1:5000/api/endpoint666'
# filename = 'leanspace.title.csv'
# filename = 'leanspace.bad.csv'

headers = {
    # 'Authorization': f'Bearer {api_not}',
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
    # etc
}

def send_api_request(payload):
    print("Payload: ", json.dumps(payload, indent=3) )
    print("Headers:", headers)
    response = requests.post(api_url, headers=headers, json=payload)

    # Check API responses
    if response.status_code == 200:
        print('API request success')
        print(response.json())
    else:
        print('API request fail')
        print(response.status_code, response.text)
        # print(response.status_code)


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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide the csv filename as an argument.")
    else:
        filename = sys.argv[1]
        process_csv_file(filename, api_url)