import requests
from google.cloud import firestore
cntr_url = "https://cntr2-ietsvmyfaq-uc.a.run.app"
api = "/A2/login"

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

# Test case for login success with response code 200
def login_success_code_200():
    login_data = {
        "Email": "aa@aa",
        "Password": "aa"
    }
    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.post((cntr_url + api), json=login_data)

    try:
        assert response.status_code == 200
        print("Test Case 1: Login Success ; Response code 200 - PASSED", green_tick)
    except AssertionError as e:
        print("Test Case 1: Login Success ; Response code 200 - FAILED:", red_cross, e)

# Test case for login failure with response code 409
def login_failure_code_404():
    login_data = {
        "Email": "fihefefeo",
        "Password": "dfnjebfk@njdvb"
    }
    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.post((cntr_url + api), json=login_data)

    try:
        assert response.status_code == 404
        print("Test Case 2: Login Failed, Exception : 'Invalid credentials / Credentials not found' ; Response code 404 - PASSED",
              green_tick)
    except AssertionError as e:
        print("Test Case 2: Login Failed, Exception : 'Invalid credentials / Credentials not found' ; Response code 404 - FAILED:",
              red_cross, e)



if __name__ == "__main__":
    # Run the test cases
    login_success_code_200()
    login_failure_code_404()

