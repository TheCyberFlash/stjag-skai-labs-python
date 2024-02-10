import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_unauthorized_sales', methods=['POST'])
def detect_unauthorized_sales():
    data = request.get_json()
    print(data)
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)