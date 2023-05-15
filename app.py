from flask import Flask, request, jsonify

app = Flask(__name__)

# Home
@app.route('/')
def index():
	return 'Leanspace Index page'

# Some API endpoint
@app.route('/api/endpoint666', methods=['POST'])
def handle_post_request():
    data = request.json
    print(data)
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON payload is not valid.'}), 400

        # Validate the required fields in the data
        if 'userID' not in data or 'sensorID' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        # Process the data as per your requirements
        print(data)
        return jsonify({'message': 'Data received and processed successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
	    # return {'message': 'Data received successfully'}


# We want the server to run locally
if __name__ == '__main__':
    app.run(debug=True)