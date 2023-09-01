import requests
from google.cloud import firestore

cntr_url = "https://cntr3-ietsvmyfaq-uc.a.run.app"
api = "/A2/sessionData/"

"""
    HTML symbols
    Reference: `HTML symbols <https://www.htmlsymbols.xyz/unicode/U+2705>`_
    
"""
green_tick = '\u2705'  # Green tick emoji
"""
    HTML symbols
    Reference: `HTML symbols <https://www.htmlsymbols.xyz/unicode/U+274C>`_
"""    
red_cross = '\u274C'  # Red cross emoji

"""
    Get started with Cloud Firestore
    Reference: `Get started with Cloud Firestore <https://firebase.google.com/docs/firestore/quickstart>`_
"""
db = firestore.Client()

def get_session_data_code_200():
    # Test case for get session data success with response code 200
    email = "aa@aa"
    session_data = {
        "Email": "aa@aa",
        "Location": "aa",
        "Name": "aa",
        "Offline": False,
        "Online": True,
        "Password": "aa",
        "Timestamp": "04:05:01, 03:July:2023, UTC"
    }
    session_api = api + email

    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.get((cntr_url + session_api))

    try:
        assert response.status_code == 200
        assert response.json() == session_data
        print("Test Case 1: Get session data Success ; Response code 200 - PASSED", green_tick)
    except AssertionError as e:
        print("Test Case 1: Get session data Success ; Response code 200 - FAILED:", red_cross, e)
        print(response.json())


def get_other_online_users_none():
    # Test case for getting other online users with no users present
    email = "aa@aa"
    
    session_api = api + "usersOnline/" + email
    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.get((cntr_url + session_api))

    try:
        response_data = response.json()
        assert len(response_data) == 0
        print("Test Case 2: Get other online users ; No users - PASSED", green_tick)
    except AssertionError as e:
        print("Test Case 2: Get other online users ; No users - FAILED:", red_cross, e)


def make_user_online():
    # Make a user online for testing purposes
    cntr2_url = "https://cntr2-ietsvmyfaq-uc.a.run.app"
    login_api = "/A2/login"
    login_data = {
        "Email": "test@test",
        "Password": "test"
    }
    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.post((cntr2_url + login_api), json=login_data)
    if response.ok:
        print("User - Vikram : Login success")
    else:
        print("User - Vikram : Login failed", response)


def get_other_online_users():
    # Test case for getting other online users with users present
    email = "aa@aa"
    
    session_api = api + "usersOnline/" + email
    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.get((cntr_url + session_api))

    try:
        response_data = response.json()
        assert len(response_data) > 0
        print("Test Case 3: Get other online users ; users_count > 0 - PASSED", green_tick)
    except AssertionError as e:
        print("Test Case 3: Get other online users ; users_count > 0 - FAILED:", red_cross, e)


#Perform cleanup operations after test cases are done
def cleanup(email):
    """
        Delete documents
        Reference: `Delete documents <https://firebase.google.com/docs/firestore/manage-data/delete-data>`_
    """
    db.collection('Reg').where('Email', '==', email).get().delete()
    db.collection('state').document(email).get().delete()

if __name__ == "__main__":
    # Run the test cases
    get_session_data_code_200()
    get_other_online_users_none()
    make_user_online()
    get_other_online_users()

    cleanup("aa@aa")
