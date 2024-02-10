import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_unauthorized_sales', methods=['POST'])
def detect_unauthorized_sales():
    data = request.get_json()

    productListings = data.get('productListings', [])
    salesTransactions = data.get('salesTransactions', [])

    unauthorized_sales = identify_unauthorized_sales(productListings, salesTransactions)
    print(unauthorized_sales)

    return identify_unauthorized_sales(productListings, salesTransactions)

def identify_unauthorized_sales(productListings, salesTransactions):
    unauthorized_sales = []

    authorized_sellers = {listing['productID']: listing['authorizedSellerID'] for listing in productListings}

    for transaction in salesTransactions:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']

        if product_id not in authorized_sellers or seller_id != authorized_sellers[product_id]:
            unauthorized_sales.append(transaction)
            
    return unauthorized_sales

if __name__ == '__main__':
    app.run(debug=True)