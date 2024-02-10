from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/interview_schedule', methods=['POST'])
def calculate_max_interviews():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract start_times and end_times from the JSON data
        start_times = data.get('start_times', [])
        end_times = data.get('end_times', [])

        # Calculate the maximum number of non-overlapping interviews
        max_interviews = calculate_interviews(start_times, end_times)
        print(max_interviews)

        # Return the result as JSON
        return jsonify({"max_interviews": max_interviews})
    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({"error": str(e)}), 400

def calculate_interviews(start_times, end_times):
    try:
        # Check for invalid input
        if not start_times or not end_times or len(start_times) != len(end_times):
            raise ValueError("Invalid input")
        
        # Sort interviews based on end times
        sorted_interviews = sorted(zip(start_times, end_times), key=lambda x: x[1])

        # Initialize variables
        max_interviews = 0
        previous_end_time = float('-inf')

        # Iterate through sorted interviews
        for start, end in sorted_interviews:
            # Check for non-overlapping interviews
            if start >= previous_end_time:
                max_interviews += 1
                previous_end_time = end

        # Return the result
        return max_interviews
    except Exception as e:
        # Raise any exceptions encountered during the calculation
        raise e

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)