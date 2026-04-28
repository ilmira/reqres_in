import allure

from services.base_api import BaseAPI
from services.reqres_in.users.models.users import CreateUserResponse
from utils.helper import Helper


class CreateUser(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Создание нового пользователя')
    def create_user(self, name: str, job: str):
        """Создание нового пользователя.

        Args:
            name (str): Имя пользователя
            job (str): Должность пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        data = {"name": name, "job": job}
        response = self.session.post(f"{self.base_url}/users", json=data)
        self.helper.attach_response(response.json())
        return response

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response, user_data):
        validated_data = CreateUserResponse.model_validate(response.json())

        assert validated_data.id
        assert validated_data.name == user_data['name']
        assert validated_data.job == user_data['job']