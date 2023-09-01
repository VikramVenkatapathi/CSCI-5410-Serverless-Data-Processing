from flask import Flask, request, jsonify
from google.cloud import firestore
from flask_cors import CORS
from google.cloud.firestore_v1.base_query import FieldFilter
# from datetime import datetime
import copy


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

user_email = ""
#API to handle logout requests
@app.route('/A2/sessionData/<email>/logout', methods=['POST'])
def logout_user(email):

    if(update_state(email)):
        return "Logout success!!",200
    else:
        return "Logout failed!!",500

#update the state of the user when logging in
def update_state(email):
    state_query_data = db.collection('state').document(email)

    try:
        # Get the current state data
        doc = state_query_data.get()
        current_data = doc.to_dict()

        #if no state is found -> ERROR
        if current_data is None:
            raise ValueError(f"No state data found for email: {email}")

        current_online_state = current_data.get('Online', True)
        current_offline_state = current_data.get('Offline', False)

        # Toggle the online and offline states
        new_online_state = not current_online_state
        new_offline_state = not current_offline_state

        # Update the document with the new states
        state_query_data.update({'Online': new_online_state, 'Offline': new_offline_state})
        """
            Get data with Cloud Firestore
            Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_
        """
        doc = state_query_data.get()
        current_data = doc.to_dict()
        # print(current_data)
        return True

    except Exception as e:
        print(f"An error occurred while updating the state: {str(e)}")
        return False

#API to handle the request to get all the other online users
@app.route('/A2/sessionData/usersOnline/<email>', methods=['GET'])
def get_users_online(email):
    online_users = [] #list of other online users
    users_ref = db.collection('state')

    """
        Get data with Cloud Firestore
        Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_
    """
    query = users_ref.where('Online', '==', True).get()

    for user_doc in query:
        user_data = user_doc.to_dict()
        online_users.append(user_doc.id)
<<<<<<< HEAD
    if(len(online_users) > 1):
        online_users.remove(email)
    return jsonify(online_users), 200

#email=<email>&password=<password>
@app.route('/A2/sessionData/', methods=['GET'])
def get_user_data():
    print("<<<<<<<<<ccc")
    email = request.args.get('email')
    password = request.args.get('password')
=======
    online_users.remove(email) #since listing only the other users, remove the current user with <email> 
    return jsonify(online_users), 200
  
#API to display the session data of the user with <email>
@app.route('/A2/sessionData/<email>', methods=['GET'])
def get_user_data(email):
>>>>>>> c46b3c7392f210c53f032949c7964b7ee77952a7
    reg_data = get_reg_data(email)

    data = copy.copy(reg_data)
    state_data = get_state_data(email) #combine the document from "Reg" & "state"
    
    data.update(state_data)
    
    return jsonify(data)

#get the "state" data of the <email>
def get_state_data(email):
    #Get data of user from collection "state"
    """
        Get data with Cloud Firestore
        Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_
    """
    state_data = {}
    state_query_data = db.collection('state').document(email).get()

    if state_query_data.exists:
        state_data = state_query_data.to_dict()

    return state_data

#get the "Reg" data of the <email>
def get_reg_data(email):
    #Get data of user from collection "Reg"
    """
        Get data with Cloud Firestore
        Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/query-data/get-data>`_
    """
    registration_ref = db.collection('Reg')
    reg_query_data = registration_ref.where(filter=FieldFilter("Email", "==", email)).get()
    reg_data = {}
    for document in reg_query_data:
        # Access the document data
        reg_data = document.to_dict()    
    return reg_data

if __name__ == "__main__":
    app.run("0.0.0.0",port=5002)



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

    Delete data from Cloud Firestore
    Reference: `Firestore Documentation <https://firebase.google.com/docs/firestore/manage-data/delete-data>`_
 
"""