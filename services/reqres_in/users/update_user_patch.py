import allure

from services.base_api import BaseAPI
from services.reqres_in.users.models.users import UpdateUserResponse
from utils.helper import Helper


class UpdateUserPatch(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Обновление данных пользователя: метод PATCH')
    def update_user_patch(self, id: int, name: str, job: str):
        """Обновление данных пользователя.

        Args:
            id (int): ID пользователя
            name (str): Имя пользователя
            job (str): Должность пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        data = {"name": name, "job": job}
        response = self.session.patch(f"{self.base_url}/users/{id}", json=data)
        self.helper.attach_response(response.json())
        return response

    def validate_data(self, response, name, job):
        with allure.step('Валидация ответа по Pydantic-схеме UpdateUserResponse'):
            validated_data = UpdateUserResponse.model_validate(response.json())
        with allure.step(f'Проверка name, ожидается {name}'):
            assert validated_data.name == name
        with allure.step(f'Проверка job, ожидается {job}'):
            assert validated_data.job == job


