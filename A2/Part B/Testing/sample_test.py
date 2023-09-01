import pytest
import unittest
from unittest.mock import Mock, patch
import requests
import sys
import os

# Add the path to the microservice1 folder
microservice1_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'microservice1'))
sys.path.append(microservice1_path)

from microservice1 import registration_handler

class FireStoreMock:
    def __init__(self):
        self.collection = Mock()

    def document(self, *args, **kwargs):
        return Mock()
    
@patch('microservice1.firestore.Client', return_value=FireStoreMock)
class TestRegistration(unittest.TestCase):
    def test_registration_handler(self, firestore_mock):
        cntr_url = "https://cntr1-ietsvmyfaq-uc.a.run.app" 
        api = "/A2/register"

        user_data = {
            "Name": "aa",
            "Password": "aa",
            "Email": "aa@aa",
            "Location": "aa"
        }

        request_mock = Mock(get_json=Mock(return_value=user_data))

        response = registration_handler(request_mock)

        # Assert the expected behavior based on the response
        self.assertEqual(response, "<<< Registration success! >>>")
        firestore_mock.assert_called_once()
        firestore_mock.return_value.collection.assert_called_with('Reg')
        firestore_mock.return_value.collection.return_value.document.return_value.set.assert_called_with({
            "Name": "aa",
            "Password": "aa",
            "Email": "aa@aa",
            "Location": "aa"
        })


def initial_test():
    cntr_url = "https://cntr1-ietsvmyfaq-uc.a.run.app" 
    api = "/A2/register"

    user_data = {
        "Name": "aa",
        "Password": "aa",
        "Email": "aa@aa",
        "Location": "aa"
    }

    response = requests.post((cntr_url+api),json=user_data)

    try:
        assert response.status_code == 409
        print("Test Case 1: POST user_data Request - Passed")
    except AssertionError as e:
        print("Test Case 1: POST user_data - Failed:", e)

if __name__ == "__main__":
    # initial_test()
    unittest.main()

