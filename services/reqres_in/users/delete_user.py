import allure

from services.base_api import BaseAPI
from utils.helper import Helper


class DeleteUser(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Удаление пользователя')
    def delete_user(self, id: int):
        """Удаление пользователя.

        Args:
            id (int): ID пользователя

        Returns:
            requests.Response: Ответ от сервера
        """
        response = self.session.delete(f"{self.base_url}/users/{id}")
        self.helper.attach_response(response.text)
        return response

    @allure.step('Проверка удаления пользователя')
    def check_delete(self, id: int):
        """Проверка удаления пользователя.

        Args:
             id (int): ID пользователя

        Returns:
             requests.Response: Ответ от сервера
        """
        response = self.session.get(f"{self.base_url}/users/{id}")
        return response
