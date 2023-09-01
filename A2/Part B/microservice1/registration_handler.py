from flask import Flask, request
from google.cloud import firestore
from flask_cors import CORS

# Initialize the Flask app
<<<<<<< HEAD
=======
"""
    Flask - (Creating first simple application)
    Reference: `Flask in Python Documentation <https://www.geeksforgeeks.org/flask-creating-first-simple-application//>`_
"""
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7
app = Flask(__name__)

"""
    Enable Flask-CORS in Python
    Reference: `Flask-CORS in Python Documentation <https://www.geeksforgeeks.org/how-to-install-flask-cors-in-python/>`_
"""
CORS(app)
# Allow specific HTTP methods (e.g., GET, POST, PUT)
CORS(app, methods=['GET', 'POST', 'PUT'])

# Allow specific headers in the request
CORS(app, headers=['Content-Type'])

# Allow cookies to be included in cross-origin requests
CORS(app, supports_credentials=True)

# Initialize Firestore client
<<<<<<< HEAD
=======
"""
    Get started with Cloud Firestore
    Reference: `Get started with Cloud Firestore <https://firebase.google.com/docs/firestore/quickstart>`_
"""
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7
db = firestore.Client()

# API to Handle registration data
@app.route('/A2/register', methods=['POST'])
def handle_registration_data():
    try:
        # Get registration data from the request
        registration_data = request.get_json()
        print("Registration data: ", "\n", registration_data, "\n")

        # Extract required fields from registration data
        name = registration_data['Name']
        password = registration_data['Password']
        email = registration_data['Email']
        location = registration_data['Location']

<<<<<<< HEAD
        # Create a new document in the 'Reg' collection
        registration_ref = db.collection('Reg').document()
        registration_ref.set({
            'Name': name,
            'Password': password,
            'Email': email,
            'Location': location
        })
=======
    # Check if the email already exists in the collection
    """
        Get data with Cloud Firestore
        Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_
    """
    email_exists = db.collection('Reg').where('Email', '==', email).get()
    if len(email_exists) > 0:
        return "<<< Email already exists! >>>", 409
    

    """
        Add data to Cloud Firestore
        Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/manage-data/add-data>`_
    """
    registration_ref = db.collection('Reg').document()
    registration_ref.set({
        'Name': name,
        'Password': password,
        'Email': email,
        'Location': location
    })
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7

        # Return success response
        return "<<< Registration success! >>>", 200

    except Exception as e:
        # Handle the exception and return an error response
        error_message = f"An error occurred: {str(e)}"
        return error_message, 500

if __name__ == "__main__":
    # Run the Flask app on 0.0.0.0:5000
<<<<<<< HEAD
    app.run("0.0.0.0", port=5000)
=======
    app.run("0.0.0.0",port=5000)


"""
All references:

    Flask - (Creating first simple application)
    Reference: `Flask in Python Documentation <https://www.geeksforgeeks.org/flask-creating-first-simple-application//>`_
    
    Enable Flask-CORS in Python
    Reference: `Flask-CORS in Python Documentation <https://www.geeksforgeeks.org/how-to-install-flask-cors-in-python/>`_

    Add data to Cloud Firestore
    Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/manage-data/add-data>`_

    Get data with Cloud Firestore
    Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_

"""
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7
