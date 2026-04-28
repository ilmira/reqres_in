import allure

from services.base_api import BaseAPI
from services.reqres_in.resources.models.resource import SingleResourceResponse
from utils.helper import Helper


class GetResource(BaseAPI):
    helper = Helper()

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Получаем ресурс по id')
    def get_resource(self, id: int):
        response = self.session.get(f"{self.base_url}/unknown/{id}")
        self.helper.attach_response(response.json())
        return response

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response):
        validated_data = SingleResourceResponse.model_validate(response.json())
