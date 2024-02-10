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

    if not start_times or not end_times or len(start_times) != len(end_times):
        raise ValueError("Invalid input")
    
    sorted_interviews = sorted(zip(start_times, end_times), key=lambda x: x[1])

    max_interviews = 0
    previous_end_time = float('-inf')

    for start, end in sorted_interviews:
        if start >= previous_end_time:
            max_interviews += 1
            previous_end_time = end
        
    return 0

if __name__ == '__main__':
    app.run(debug=True)