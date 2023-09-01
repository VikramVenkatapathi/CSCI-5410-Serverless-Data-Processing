from flask import Flask, request
from google.cloud import firestore
from flask_cors import CORS
from google.cloud.firestore_v1.base_query import FieldFilter
import datetime
import pytz

# Initialize the Flask app
"""
    Flask - (Creating first simple application)
    Reference: `Flask in Python Documentation <https://www.geeksforgeeks.org/flask-creating-first-simple-application//>`_
"""
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

"""
    Get started with Cloud Firestore
    Reference: `Get started with Cloud Firestore <https://firebase.google.com/docs/firestore/quickstart>`_
"""
db = firestore.Client()

@app.route('/A2/login', methods=['POST'])
def authenticate_user():
    # Get login data from the request
    login_data = request.get_json()
    print("Login data : ","\n",login_data,"\n")

    # Extract email and password from the login data
    login_email = login_data['Email']
    login_password = login_data['Password']

    registration_ref = db.collection('Reg')

    # Query Firestore to find matching user data based on email and password
    """
        Get data with Cloud Firestore
        Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_
    """
    query_data = registration_ref.where(filter=FieldFilter("Email", "==", login_email)).where(filter=FieldFilter('Password', '==', login_password)).get()

    if len(query_data) == 0:
        # If no matching user data found, return login failed response
        return "<<< Login failed! >>>", 404
    else:
        # If matching user found, update login status
        update_login_status(query_data)

    return "<<< Login success! >>>", 200

def update_login_status(query_data):
    doc_ID = ""
    for document in query_data:
        # Access the document data
        data = document.to_dict()
        # Extract the email field
        email = data.get('Email')
        if email:
            doc_ID = email

    state_ref = db.collection('state')
    state_query_data = state_ref.where(filter=FieldFilter("Email", "==", doc_ID)).get()

    time_stamp = get_timestamp()

    if(len(state_query_data) == 0):
        # If login status does not exist, create a new document and set 'Online' field to True
        """
            Add data to Cloud Firestore
            Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/manage-data/add-data>`_
        """
        state_doc_ref = state_ref.document(doc_ID)
        state_doc_ref.set({
            'Online': True,
            'Offline': False,
            'Timestamp': time_stamp
        })
    else:
        # If login status exists, update 'Online' field to True and update 'Timestamp' field
        state_doc_ref.update({
            'Online': True,
            'Timestamp': time_stamp
        })

    print(state_doc_ref.get().to_dict())

    return "<<< YOU ARE ONLINE! >>>", 200

#get the current system time
"""
    How to Get the Current Time in Python with Datetime
    Reference: `freeCodeCamp.org <https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime>`_
"""
def get_timestamp(): 
    system_time = datetime.datetime.now()
    system_timezone = datetime.datetime.now(pytz.timezone('UTC')).astimezone().tzinfo

    if system_timezone == pytz.UTC:
        formatted_time = system_time.strftime("%H:%M:%S, %d:%B:%Y, %Z")
    else:
        localized_time = system_time.astimezone(system_timezone)
        formatted_time = localized_time.strftime("%H:%M:%S, %d:%B:%Y, %Z")
    return str(formatted_time)

if __name__ == "__main__":
    # Run the Flask app on 0.0.0.0:5001
    app.run("0.0.0.0", port=5001)


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

    How to Get the Current Time in Python with Datetime
    Reference: `freeCodeCamp.org <https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime>`_

"""
