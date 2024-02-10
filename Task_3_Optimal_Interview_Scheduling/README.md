## Optimal Job Interview Scheduling API

### Intro

This Python API provides an endpoint for calculating the maximum number of non-overlapping job interviews a person can attend. The API processes POST requests containing start times and end times of job interviews, and it returns the calculated maximum number of interviews.

### Assumptions

1. **Input Format:** Assume that the input JSON data provided in the POST request follows the specified format, with "start_times" and "end_times" as the key names.

2. **Data Integrity:** Assume that the provided data is valid and that each start and end time is correctly formatted.

3. **Non-Negative Times:** Assume that all start times are less than or equal to their corresponding end times.

4. **Time Unit:** Assume that the time units used for start and end times are consistent.

### Instructions

1. **Clone the Repository:**
   - Clone this repository to your local machine.

2. **Navigate to the Project Folder:**
   - Open a terminal and navigate to the project folder using the `cd` command.

3. **Run the API:**
   - Execute the following command to run the API:

     ```bash
     python Optimal_Job_Interview_Scheduling.py
     ```

4. **Make POST Requests:**
   - Use a tool like `curl` or a programming language library (e.g., Python `requests`) to make POST requests to the API endpoint:

     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"start_times": [...], "end_times": [...]}'
     http://localhost:5000/interview_schedule
     ```

### API Response

The API responds with a JSON object containing the calculated maximum number of non-overlapping interviews.

```json
{
  "max_interviews": 3
}
```

### Error Handling

If an error occurs during processing, the API returns a JSON object with an error message and an appropriate HTTP status code.

```json
{
  "error": "Description of the error."
}
```


## Additional Notes

- If any issues arise, ensure that the input JSON data follows the specified format.
- The API follows RESTful principles and responds with appropriate HTTP status codes (e.g., 200 OK for successful requests, 400 Bad Request for invalid input).