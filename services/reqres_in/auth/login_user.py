from services.base_api import BaseAPI
from services.reqres_in.auth.models.auth import LoginRequest


class LoginUser(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    def login_user(self, login_data: LoginRequest, not_valid=False):
        if not_valid:
            data = {"email": login_data.email}
        else:
            data = {"email": login_data.email, "password": login_data.password}
        response = self.session.post(f"{self.base_url}/register", json=data)
        return response
