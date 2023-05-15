from flask import Flask, request

app = Flask(__name__)

# Home
@app.route('/')
def index():
	return 'Leanspace Index page'

# Some API endpoint
@app.route('/api/endpoint666', methods=['POST'])
def handle_post_request():
    data = request.json
    # Process the data as per your requirements
    print(data)
    return {'message': 'Data received successfully'}

# We want the server to run locally
if __name__ == '__main__':
    app.run(debug=True)