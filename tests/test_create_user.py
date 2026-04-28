import allure
import pytest

@pytest.mark.smoke
@pytest.mark.regression
@allure.title('Тест успешного создания пользователя')
@allure.testcase("https://example.com/testcase/15", "Test-15")
def test_create_user(user_factory, user_data, app):
    new_user_response = user_factory(user_data['name'], user_data['job'])
    app.create.check_status_code_is_201(new_user_response)

    app.create.validate_data(new_user_response, user_data)

