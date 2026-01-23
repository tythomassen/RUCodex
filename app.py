from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
# Allows any website (like Google AI Studio) to call this API
CORS(app)

RUTGERS_COURSES_API = "https://sis.rutgers.edu/soc/api/courses.json"
RUTGERS_OPEN_API = "https://sis.rutgers.edu/soc/api/openSections.json"

@app.route('/')
def home():
    return "Rutgers Proxy Server is Live on Port 8000!"

@app.route('/api/courses', methods=['GET'])
def get_courses():
    params = request.args
    try:
        response = requests.get(RUTGERS_COURSES_API, params=params)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/open-sections', methods=['GET'])
def get_open_sections():
    params = request.args
    try:
        response = requests.get(RUTGERS_OPEN_API, params=params)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Changed to 8000 to avoid Mac AirPlay conflict
    # host='0.0.0.0' makes it accessible through the tunnel
    app.run(debug=True, port=8000, host='0.0.0.0')