import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/interview_schedule', methods=['POST'])
def calculate_max_interviews():
    data = request.get_json()
    start_times = data.get('start_times', [])
    end_times = data.get('end_times', [])
    print(start_times)
    print(end_times)
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)