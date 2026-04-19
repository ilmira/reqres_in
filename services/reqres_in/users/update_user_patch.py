from services.base_api import BaseAPI


class UpdateUserPatch(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

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
        return response