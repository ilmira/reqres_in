import allure
import pytest

@pytest.mark.smoke
@pytest.mark.regression
@allure.title('Тест успешного просмотра данных пользователя')
@allure.testcase("https://example.com/testcase/16", "Test-16")
@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_get_user(user_id, app):
    response = app.get_class.get_user(user_id)
    app.get_class.check_status_code_is_200(response)

    app.get_class.validate_data(response, user_id)


