from unittest.mock import patch
import allure
import pytest

@pytest.mark.smoke
@pytest.mark.regression
@allure.title('Тест успешного mock')
@allure.testcase("https://example.com/testcase/17", "Test-17")
@patch('requests.get')
def test_mock_success(mock, app):
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

    response = app.get.get_user(2)
    app.get.check_status_code_is_200(response)
    app.get.check_user_data(response)

@pytest.mark.smoke
@pytest.mark.regression
@allure.title('Тест неуспешного mock')
@allure.testcase("https://example.com/testcase/18", "Test-18")
@patch('requests.get')
def test_mock_not_valid(mock, app):
    mock_response = {}
    mock.return_value.status_code = 404
    mock.return_value.json.return_value = mock_response

    response = app.get.get_user(23)
    app.get.check_status_code_is_404(response)
    app.get.check_user_data(response, valid=False)
