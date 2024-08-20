# Import necessary modules
from flask import Flask, render_template, request, redirect # Flask for web app, render_template for rendering HTML templates, request to handle form data, redirect to a different route.
from pymongo import MongoClient # MongoClient to connect to MongoDB

# Initialize the Flask application
app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client.surveydb
collection = db.survey

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html') # Render and return the 'index.html' template when the home page is accessed


# Define the route to handle form submission
@app.route('/submit', methods=['POST']) # This route listens for POST requests at the '/submit' URL
def submit():
    # Extract form data and store it in a dictionary
    data = {
        'age': request.form['age'],
        'gender': request.form['gender'],
        'total_income': request.form['total_income'],
        'expenses': {
            'utilities': request.form['utilities'],
            'entertainment': request.form['entertainment'],
            'school_fees': request.form['school_fees'],
            'shopping': request.form['shopping'],
            'healthcare': request.form['healthcare']
        }
    }
    # Insert the form data into the MongoDB collection
    collection.insert_one(data) # Insert the data dictionary into the 'survey' collection
    # Redirect to teh home page after form submission
    return redirect('/') # Redirect the user to the home page after submittine the form

# Run the Flask appllication
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) # Run the app on all available IP addresses (0.0.0.0) at port 80
