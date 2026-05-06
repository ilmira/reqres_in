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

    def validate_data(self, response, user_data):
        with allure.step('Валидация ответа по Pydantic-схеме CreateUserResponse'):
            validated_data = CreateUserResponse.model_validate(response.json())
        with allure.step('Проверка наличия id'):
            assert validated_data.id
        with allure.step(f'Проверка name, ожидается {user_data["name"]}'):
            assert validated_data.name == user_data['name']
        with allure.step(f'Проверка job, ожидается {user_data["job"]}'):
            assert validated_data.job == user_data['job']
