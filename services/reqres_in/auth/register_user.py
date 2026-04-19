from services.base_api import BaseAPI
from services.reqres_in.auth.models.auth import RegisterRequest


class RegisterUser(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    def register_user(self, register_data: RegisterRequest, not_valid=False):
        """Регистрация пользователя.
        """
        if not_valid:
            data = {"email": register_data.email}
        else:
            data = {"email": register_data.email, "password": register_data.password}
        response = self.session.post(f"{self.base_url}/register", json=data)
        return response
