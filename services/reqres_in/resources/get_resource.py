from services.base_api import BaseAPI


class GetResource(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    def get_resource(self, id: int):
        response = self.session.get(f"{self.base_url}/unknown/{id}")
        return response
