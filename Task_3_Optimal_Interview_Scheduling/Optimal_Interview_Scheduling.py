import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/interview_schedule', methods=['POST'])
def calculate_max_interviews():
    data = request.get_json()
    print(data)
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)