from flask import Flask, jsonify, send_from_directory
from store import get_sample_data
# Import any helper functions you create in store.py

app = Flask(__name__, static_folder='../client', static_url_path='')

# TASK: Define a route for "/"
# This should return index.html from the static folder
@app.route("/", methods=["GET"])
def index():
	return send_from_directory(app.static_folder, "index.html")

# TASK: Define a route for "/api/data"
# This should return a JSON object with a message and status
# Hint: You can use a function from store.py to generate the response
@app.route("/api/data", methods=["GET"])
def get_data():
	return jsonify(get_sample_data()), 200

if __name__ == '__main__':
	app.run(debug=True)
