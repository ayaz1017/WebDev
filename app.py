from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if needed
db = client['fitness_db']  # Replace with your database name
customers_collection = db['customers']  # Collection for customers

# Route for customer registration form
@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        # Get form data
        cust_name = request.form['custName']
        cust_age = request.form['custAge']
        cust_phone = request.form['custPhone']
        cust_email = request.form['custEmail']

        # Insert customer into MongoDB
        customers_collection.insert_one({
            'name': cust_name,
            'age': cust_age,
            'phone': cust_phone,
            'email': cust_email
        })

        return redirect('/success')

    return render_template('customer.html')

# Route for success page after registration
@app.route('/success')
def success():
    return "Customer Registered Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
