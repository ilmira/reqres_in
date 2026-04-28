import allure

from services.base_api import BaseAPI
from services.reqres_in.users.models.users import UpdateUserResponse
from utils.helper import Helper


class UpdateUserPut(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Обновление данных пользователя: метод PUT')
    def update_user_put(self, id: int, name: str, job: str):
        """Обновление данных пользователя.

        Args:
            id (int): ID пользователя
            name (str): Имя пользователя
            job (str): Должность пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        data = {"name": name, "job": job}
        response = self.session.put(f"{self.base_url}/users/{id}", json=data)
        self.helper.attach_response(response.json())
        return response

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response):
        validated_data = UpdateUserResponse.model_validate(response.json())