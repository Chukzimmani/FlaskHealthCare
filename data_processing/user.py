# Import necessary modules

import csv # For reading and writing CSV files
import pymongo # For interacting with MongoDB

# Define a User class to represent user data
class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age # User's age
        self.gender = gender # User's gender
        self.total_income = total_income # User's total income
        self.expenses = expenses # Dictionary of user's expenses

# Function to fetch data from MongoDB
def fetch_data():
    # Connect to the MongoDB Server
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Select the 'user_data' database
    db = client["user_data"]
    # Select (or create) the 'expenses' collection within the 'user_data' database
    collection = db["expenses"] 

    # List to store User objects
    users = []
    # Retrieve all documents from the collection
    for data in collection.find():
        # Create a User object for each document
        user = User(
            age=data['age'], # Get age from document
            gender=data['gender'], # Get gender from document
            total_income=data['total_income'], # Get total_income from document
            expenses=data['expenses'] # Get expenses dictionary from document
        )
        # Append the User object to the users list
        users.append(user)
    return users # Return the list of User objects

# Function to save user data to a CSV file
def save_to_csv(users, filename):
    # Open (or create) a CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        # Define the field name (column headers) for the CSV file
        fieldnames = ['age', 'gender', 'total_income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        # Create a DictWriter object for writing dictionaries to the CSV file
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row to the CSV file
        writer.writeheader()
        # Write user data to the CSV file
        for user in users:
            writer.writerow({
                'age': user.age, # Write age
                'gender': user.gender,# Write gender
                'total_income': user.total_income, # Write income
                'utilities': user.expenses.get('utilities', ''), # Write utilities expense (empty string if not present)
                'entertainment': user.expenses.get('entertainment', ''), # Write entertainment expense (empty string if not present)
                'school_fees': user.expenses.get('school_fees', ''), # Write school fees expense (empty string if not present)
                'shopping': user.expenses.get('shopping', ''),  # Write shopping expense (empty string if not present)
                'healthcare': user.expenses.get('healthcare', '') # Write healthcare expense (empty string if not present)
            })
# Main execution block
if __name__ == '__main__':
    users = fetch_data() # Fetch user data from MongoDB
    save_to_csv(users, 'user_data.csv') # Save user data to 'user_data.csv'
