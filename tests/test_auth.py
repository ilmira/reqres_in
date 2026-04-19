import allure
import pytest

from services.reqres_in.auth.login_user import LoginUser
from services.reqres_in.auth.models.auth import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse
from services.reqres_in.auth.register_user import RegisterUser
from utils.helper import Helper


@allure.feature('Auth')
class TestAuth:
    helper = Helper()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест успешной регистрации')
    @allure.testcase("https://example.com/testcase/11", "Test-11")
    def test_registration(self, env_config):
        register_user_data = RegisterRequest(email='eve.holt@reqres.in', password='pistol')
        with allure.step('Регистрация пользователя'):
            response = RegisterUser(env_config).register_user(register_user_data)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = RegisterResponse.model_validate(response.json())
            assert validated_data.id > 0
            assert validated_data.token

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест неуспешной регистрации')
    @allure.testcase("https://example.com/testcase/12", "Test-12")
    def test_not_valid_registration(self, env_config):
        register_user_data = RegisterRequest(email='example@test.tst', password='1234')
        with allure.step('Регистрация пользователя'):
            response = RegisterUser(env_config).register_user(register_user_data, not_valid=True)

        with allure.step('Проверяем статус код'):
            assert response.status_code == 400

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест успешного входа')
    @allure.testcase("https://example.com/testcase/13", "Test-13")
    def test_login(self, env_config):
        register_user_data = RegisterRequest(email='eve.holt@reqres.in', password='pistol')
        with allure.step('Регистрация пользователя'):
            response = RegisterUser(env_config).register_user(register_user_data)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = RegisterResponse.model_validate(response.json())
            assert validated_data.id > 0
            assert validated_data.token
        login_user = LoginRequest(email=register_user_data.email, password=register_user_data.password)
        with allure.step('Авторизация пользователя'):
            response = LoginUser(env_config).login_user(login_user)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = LoginResponse.model_validate(response.json())
            assert validated_data.token

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Тест неуспешного входа')
    @allure.testcase("https://example.com/testcase/14", "Test-14")
    def test_not_valid_login(self, env_config):
        register_user_data = RegisterRequest(email='eve.holt@reqres.in', password='pistol')
        with allure.step('Регистрация пользователя'):
            response = RegisterUser(env_config).register_user(register_user_data)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = RegisterResponse.model_validate(response.json())
            assert validated_data.id > 0
            assert validated_data.token
        login_user = LoginRequest(email=register_user_data.email, password=register_user_data.password)
        with allure.step('Авторизация пользователя без пароля'):
            response = LoginUser(env_config).login_user(login_user, not_valid=True)

        with allure.step('Проверяем статус код'):
            assert response.status_code == 400
