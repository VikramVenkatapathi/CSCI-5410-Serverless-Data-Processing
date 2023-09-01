import requests


cntr_url = "https://cntr1-ietsvmyfaq-uc.a.run.app"
api = "/A2/register"

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


# Test case for registration success with response code 200
def registration_success_code_200(user_data):

    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.post((cntr_url + api), json=user_data)

    try:
        assert response.status_code == 200
        print("Test Case 1: Registration Success ; Response code 200 - PASSED", green_tick)
    except AssertionError as e:
        print("Test Case 1: Registration Success ; Response code 200 - FAILED:", red_cross, e)


# Test case for registration failure with response code 409
def registration_failure_code_409(user_data):
   
    """
        Flask HTTP methods
        Reference: `Flask HTTP methods, handle GET & POST requests <https://pythonbasics.org/flask-http-methods/>`_
    """
    response = requests.post((cntr_url + api), json=user_data)

    try:
        assert response.status_code == 409
        print("Test Case 2: Registration Failed, Exception : 'Email already exists' ; Response code 409 - PASSED",
              green_tick)
    except AssertionError as e:
        print("Test Case 2: Registration Failed, Exception : 'Email already exists' ; Response code 409 - FAILED:",
              red_cross, e)



if __name__ == "__main__":
    user_data = {
        "Name": "aa",
        "Password": "aa",
        "Email": "aa@aa",
        "Location": "aa"
    }

    # Run the test cases
    registration_success_code_200(user_data)
    registration_failure_code_409(user_data)
