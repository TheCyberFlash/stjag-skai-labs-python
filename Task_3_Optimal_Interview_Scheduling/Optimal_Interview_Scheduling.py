import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/interview_schedule', methods=['POST'])
def calculate_max_interviews():
    data = request.get_json()

    start_times = data.get('start_times', [])
    end_times = data.get('end_times', [])

    max_interviews = calculate_interviews(start_times, end_times)
    print(max_interviews)

    return jsonify({"max_interviews": max_interviews})

def calculate_interviews(start_times, end_times):
    return 0

if __name__ == '__main__':
    app.run(debug=True)