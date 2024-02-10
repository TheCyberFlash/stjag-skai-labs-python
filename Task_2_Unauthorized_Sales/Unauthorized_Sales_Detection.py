from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_unauthorized_sales', methods=['POST'])
def detect_unauthorized_sales():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract product listings and sales transactions from the JSON data
        productListings = data.get('productListings', [])
        salesTransactions = data.get('salesTransactions', [])

        # Identify unauthorized sales using the provided function
        unauthorized_sales = identify_unauthorized_sales(productListings, salesTransactions)
        print(unauthorized_sales)

        # Prepare the response with unauthorized sales information
        response = {'unauthorizedSales': unauthorized_sales}
        
        # Return the response as JSON with a 200 OK status
        return jsonify(response), 200
    except Exception as e:
        # Handle exceptions and return an error response with a 400 Bad Request status
        return jsonify({'error': str(e)}), 400

def identify_unauthorized_sales(productListings, salesTransactions):
    unauthorized_sales = []

    # Create a dictionary of authorized sellers based on product ID
    authorized_sellers = {listing['productID']: listing['authorizedSellerID'] for listing in productListings}

    # Check each sales transaction for unauthorized sales
    for transaction in salesTransactions:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']

        # Identify unauthorized sales based on product ID and seller ID mismatch
        if product_id not in authorized_sellers or seller_id != authorized_sellers[product_id]:
            unauthorized_sales.append(transaction)

    # Return the list of unauthorized sales
    return unauthorized_sales

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)