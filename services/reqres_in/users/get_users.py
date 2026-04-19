from services.base_api import BaseAPI


class GetUsers(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    def get_users(self, page_number: int):
        """Получить список пользователей.

        Args:
            page_number (int): номер страницы

        Returns:
            requests.Response: Ответ от сервера
        """
        response = self.session.get(f"{self.base_url}/users?page={page_number}")

        return response