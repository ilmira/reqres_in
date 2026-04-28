import allure

from services.base_api import BaseAPI
from services.reqres_in.resources.models.resource import ResourcesListResponse
from utils.helper import Helper


class GetResources(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Получаем список ресурсов')
    def get_resources(self):
        response = self.session.get(f"{self.base_url}/unknown")
        self.helper.attach_response(response.json())
        return response

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response):
        validated_data = ResourcesListResponse.model_validate(response.json())
        assert len(validated_data.data) == validated_data.per_page
