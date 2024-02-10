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


## Additional Notes

- If any issues arise, ensure that the input JSON data follows the specified format.
- The API follows RESTful principles and responds with appropriate HTTP status codes (e.g., 200 OK for successful requests, 400 Bad Request for invalid input).