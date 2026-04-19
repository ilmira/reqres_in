from unittest.mock import patch
import requests


def process_user_data(user_id: int):
    return requests.get(f'https://reqres.in/api/users/{user_id}')

@patch('requests.get')
def test_mock_success(mock):
    mock_response = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        }
    }
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = mock_response

    response = process_user_data(2)
    assert response.status_code == 200
    assert response.json()['data']['id']
    assert response.json()['data']['id'] == 2

@patch('requests.get')
def test_mock_not_valid(mock):
    mock_response = {}
    mock.return_value.status_code = 404
    mock.return_value.json.return_value = mock_response

    response = process_user_data(23)
    assert response.status_code == 404
    assert not response.json()
