---

# Task One - Display a Polygon on a Map

## Display Polygon on a Map

### Intro

This web application uses the OpenLayers library to display a polygon on a map. The polygon coordinates are fetched from the "polygon.json" file, and the map is rendered accordingly.

### Assumptions

Assume the polygon.json file contains valid geo-coordinates in the required format.

### Instructions

1. **Clone the Repository:**

   - Clone this repository to your local machine.

2. **Navigate to the Project Folder:**

   - Open a terminal and navigate to the project folder using the `cd` command.

3. **Start a Local Server:**

   - Start a simple Python web server by running the command:
     ```bash
     python -m http.server
     ```

4. **Open the Application:**
   - Open a web browser and visit [http://localhost:8000/index.html](http://localhost:8000/index.html).

### Additional Notes

- If any issues arise, ensure that the "polygon.json" file is present and contains valid geo-coordinates.
- Adjustments to the zoom level are automatically made to fit the entire polygon on the map.
- For more information, refer to the comments in the `app.js` file.

Try it here [Github Page](https://thecyberflash.github.io/stjag-skai-labs-python/) 

---

# Task Two - Unauthorized Sales Detection

## Unauthorized Sales Detection API

### Intro

This Python API provides an endpoint for detecting unauthorized sales transactions from provided datasets of product listings and actual sales records. The API compares product listings against sales transactions to identify any unauthorized sales and returns the results in a specified format.

### Assumptions

1. **Input Format:** Assume that the input JSON data provided in the POST request follows the specified format, with "productListings" and "salesTransactions" as the key names.

2. **Data Integrity:** Assume that the provided data is valid and that each product and seller ID exists and is correctly formatted.

3. **Unique Product IDs:** Assume that each product has a unique product ID within the given data.

4. **Seller Authorization:** Assume that each product listing includes a valid and authorized seller ID.

### Instructions

1. **Clone the Repository:**
   - Clone this repository to your local machine.

2. **Navigate to the Project Folder:**
   - Open a terminal and navigate to the project folder using the `cd` command.

3. **Run the API:**
   - Execute the following command to run the API:

     ```bash
     python Unauthorized_Sales_Detection.py
     ```

4. **Make POST Requests:**
   - Use a tool like `curl` or a programming language library (e.g., Python `requests`) to make POST requests to the API endpoint:

     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"productListings": [...], "salesTransactions": [...]}'
     http://localhost:5000/detect_unauthorized_sales
     ```

### API Response

The API responds with a JSON object containing unauthorized sales information.

```json
{
  "unauthorizedSales": [
    {"productID": "123", "unauthorizedSellerID": ["B2"]}
  ]
}
```

### Error Handling

If an error occurs during processing, the API returns a JSON object with an error message and an appropriate HTTP status code.

```json
{
  "error": "Description of the error."
}
```


### Additional Notes

- If any issues arise, ensure that the input JSON data follows the specified format.
- The API follows RESTful principles and responds with appropriate HTTP status codes (e.g., 200 OK for successful requests, 400 Bad Request for invalid input).

---

# Task Three

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

---
