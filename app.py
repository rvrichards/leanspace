from flask import Flask, request, jsonify

app = Flask(__name__)


valid_api_keys = { 'JamesBond007',  'SomeOtherSecretKey'}

# Home
@app.route('/')
def index():
    return 'Leanspace Index page'

# Some API endpoint
@app.route('/api/endpoint666', methods=['POST'])
def handle_post_request():
    print("Inside APP")

    auth_header = request.headers.get('Authorization')

    if auth_header:
        # Extract the API key from Auth header
        api_key = auth_header.split(' ')[1] if len(auth_header.split(' ')) > 1 else None
        print("api-key: ======", api_key)
        # Check if the API key is valid
        if api_key and api_key in valid_api_keys:
            data = request.json
            print(data)
            try:
                data = request.get_json()
                if not data:
                    return jsonify({'error': 'JSON payload is not valid.'}), 400

                # Validate the required fields in the data
                if 'userID' not in data or 'sensorID' not in data:
                    return jsonify({'error': 'Missing required fields (userID or sensorID)'}), 400

                # Process the data as per your requirements
                print(data)
                return jsonify({'message': 'Data received and processed successfully'}), 200
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        # Return a response indicating authentication failure
        return jsonify({'message': 'Authentication failed'}), 401





# We want the server to run locally
if __name__ == '__main__':
    app.run(debug=True)