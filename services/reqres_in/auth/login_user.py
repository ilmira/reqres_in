import allure

from services.base_api import BaseAPI
from services.reqres_in.auth.models.auth import LoginRequest, LoginResponse
from utils.helper import Helper


class LoginUser(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    def login_user(self, login_data: LoginRequest, not_valid=False):
        if not_valid:
            data = {"email": login_data.email}
            about_password = ''
        else:
            data = {"email": login_data.email, "password": login_data.password}
            about_password = 'без пароля'

        with allure.step('Авторизация пользователя' + about_password):
            response = self.session.post(f"{self.base_url}/register", json=data)
            self.helper.attach_response(response.json())
            return response

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response):
        validated_data = LoginResponse.model_validate(response.json())
        assert validated_data.token
