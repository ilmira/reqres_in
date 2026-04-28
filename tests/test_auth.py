import allure
import pytest

from conftest import register_data_valid
from services.reqres_in.auth.models.auth import RegisterRequest, LoginRequest


@allure.feature('Auth')
class TestAuth:

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест успешной регистрации')
    @allure.testcase("https://example.com/testcase/11", "Test-11")
    def test_registration(self, app, register_data_valid):
        response = app.register.register_user(register_data_valid)
        app.register.check_status_code_is_200(response)
        app.register.validate_data(response)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест неуспешной регистрации')
    @allure.testcase("https://example.com/testcase/12", "Test-12")
    def test_not_valid_registration(self, app):
        register_user_data = RegisterRequest(email='example@test.tst', password='1234')
        response = app.register.register_user(register_user_data, not_valid=True)

        app.register.check_status_code_is_400(response)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест успешного входа')
    @allure.testcase("https://example.com/testcase/13", "Test-13")
    def test_login(self, app, register_data_valid):
        response = app.register.register_user(register_data_valid)

        app.register.check_status_code_is_200(response)
        app.register.validate_data(response)

        login_user = LoginRequest(email=register_data_valid.email, password=register_data_valid.password)
        response = app.login.login_user(login_user)

        app.login.check_status_code_is_200(response)
        app.login.validate_data(response)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест неуспешного входа')
    @allure.testcase("https://example.com/testcase/14", "Test-14")
    def test_not_valid_login(self, app, register_data_valid):
        response = app.register.register_user(register_data_valid)

        app.register.check_status_code_is_200(response)
        app.register.validate_data(response)
        login_user = LoginRequest(email=register_data_valid.email, password=register_data_valid.password)
        response = app.login.login_user(login_user, not_valid=True)

        app.login.check_status_code_is_400(response)
